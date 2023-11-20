# Програма-банкомат.
#    Використувуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль
#       (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл
#       <{username}_balance.TXT>) та історію транзакцій (файл
#       <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх.
#       Обов'язкова перевірка введених даних (введено цифри; знімається
#       не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу
#       (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка
#       додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете
#       реалізувати функціонал додавання нового користувача - не
#       стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь
#       workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує
#       ім'я/пароль). Якщо вони неправильні - вивести повідомлення
#       про це і закінчити роботу (хочете - зробіть 3 спроби, а потім
#       вже закінчити роботу - все на ентузіазмі :))
#       - потім - елементарне меню типн:
#         Введіть дію:
#            1. Продивитись баланс
#            2. Поповнити баланс
#            3. Вихід
#       - далі - фантазія і креатив, можете розширювати функціонал, але
#       основне завдання має бути повністю реалізоване :)
#     P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt,
#     json відповідно)
#     P.S.S. Добре продумайте структуру програми та функцій (edited)


import sqlite3 as sql
import sys


class InvalidUser(Exception):
    pass


class NegativeBalance(Exception):
    pass


class InvalidAction(Exception):
    pass


class NegativeField(Exception):
    pass


def login_validation(name_argument, password_argument):
    users = get_users()

    return any(user.get(name_argument) == password_argument for user in users)


def is_admin(name_argument, password_argument):
    return name_argument == "admin" and password_argument == "admin"


def create_validation(name_argument, password_argument):
    length_name = len(name_argument)
    length_password = len(password_argument)

    is_digit = any(char.isdigit() for char in password_argument)
    is_upper_case = any(char.isupper() for char in password_argument)

    if not 3 <= length_name <= 20:
        raise InvalidUser("user name must be in range 3 - 20")
    if not length_password >= 8:
        raise InvalidUser("user password must be more 8 symbols")
    if not is_digit:
        raise InvalidUser("password has not digit")
    if not is_upper_case:
        raise InvalidUser("password has not upper symbol")
    if login_validation(name_argument, password_argument):
        raise InvalidUser("user has been exists")
    return True


def get_users():
    with sql.connect("users.db") as connection:
        cursor = connection.execute('SELECT * FROM users')
        users = cursor.fetchall()
        users_list = [{i[0]: i[1] for i in users}]

        return users_list


def get_cash_machine():
    with sql.connect("users.db") as connection:
        cursor = connection.execute('SELECT value, count FROM cash_machine')
        users = cursor.fetchall()

        cash_machine = {i[0]: i[1] for i in users}

        return cash_machine


def change_cash_machine(machine):
    with sql.connect("users.db") as connection:
        cursor = connection.cursor()

        for key, value in machine.items():
            cursor.execute("""
                UPDATE cash_machine
                SET count = ?
                WHERE value = ?
            """, (value, key))


def get_user_balance(name):
    with sql.connect("users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT balance 
            FROM users
            WHERE name == ?
        """, (name,))
        connection.commit()

        return cursor.fetchone()[0]


def set_user_balance(name, type_operation, amount, balance):
    with sql.connect("users.db") as connections:
        cursor = connections.cursor()
        cursor.execute("""
            UPDATE users
            SET balance = ?
            WHERE name = ?
        """, (balance, name))

    set_transaction(name, type_operation, amount)


def set_transaction(name, type_operation, amount):
    user_id = get_user_by_id(name)

    with sql.connect("users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions (type, total, user_id)
            VALUES (?, ?, ?)
        """, (type_operation, amount, user_id))


def get_user_by_id(name):
    with sql.connect("users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT user_id
            FROM users
            WHERE name = ?
        """, (name,))

        return cursor.fetchone()[0]


def get_minimum_denomination():
    with sql.connect("users.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT value
            FROM cash_machine
        """)

        minimum_denomination = min(cursor.fetchall())

        return minimum_denomination[0]


def replenish_balance(name):
    deposit_amount = float(input("input the amount you want to deposit: "))
    minimum_denomination = get_minimum_denomination()
    rest = deposit_amount % minimum_denomination

    if deposit_amount < 0:
        raise NegativeField("deposit_amount must be positive")
    if rest != 0:
        print("take the rest of ", rest)

    balance = get_user_balance(name)
    new_balance = str(balance + deposit_amount - rest)
    set_user_balance(name, "replenishment", deposit_amount, new_balance)


def take_balance(name):
    deposit_amount = float(input("input the amount you want to take: "))
    balance = get_user_balance(name)
    get_money = 0
    cash_machine = get_cash_machine()

    if deposit_amount < 0:
        raise NegativeField("deposit_amount must be positive")
    if deposit_amount > balance:
        raise NegativeBalance("deposit_amount must be < then balance")

    for i in cash_machine:
        while deposit_amount >= i:
            if cash_machine[i] == 0:
                break
            get_money += i
            deposit_amount -= i
            cash_machine[i] -= 1

    if deposit_amount == 0:
        new_balance = balance - get_money
        change_cash_machine(cash_machine)
        set_user_balance(name, "withdrawalad", get_money, new_balance)
    else:
        raise InvalidAction("cash_machine has not enough money or banknotes")


def get_command(func, *args, **kwargs):
    while True:
        try:
            func(*args, **kwargs)
        except NegativeBalance as e:
            print(str(e))
            continue
        except InvalidAction as e:
            print(str(e))
            continue
        except ValueError:
            print("value must be number")
            continue
        except NegativeField as e:
            print(str(e))
            continue
        else:
            break


def user_command(name):
    while True:
        action = int(input("""Введіть дію:
                               1. Продивитись баланс
                               2. Поповнити баланс
                               3. Зняти гроші
                               4. Вихід
                           """))

        match action:
            case 1:
                print(get_user_balance(name))
            case 2:
                replenish_balance(name)
            case 3:
                take_balance(name)
            case 4:
                return
            case _:
                raise InvalidAction("a non-existent action is entered")


def admin_command():
    while True:
        action = int(input("""input action
                    1 - to see cash machine balance
                    2 - change number of banknotes
                    3 - exit
                """))

        match action:
            case 1:
                print(get_cash_machine())
            case 2:
                change_number_banknote()
            case 3:
                sys.exit()
            case _:
                raise InvalidAction("a non-existent action is entered")


def start_command():
    while True:
        choice = int(input(""" input action
            1 - log in
            2 - registration
            3 - exit
        """))

        match choice:
            case 1:
                login()
            case 2:
                create_user()
            case 3:
                break
            case _:
                raise InvalidAction("a non-existent action is entered")


def admin_panel(name):
    action = int(input(""" input action
                1 - log in as a collector
                2 - log in as a user
                3 - exit
            """))

    match action:
        case 1:
            get_command(admin_command)
        case 2:
            get_command(user_command, name)
        case 3:
            sys.exit()
        case _:
            raise InvalidAction("a non-existent action is entered")


def change_number_banknote():
    cash_machine = get_cash_machine()

    for value, count in cash_machine.items():
        while True:
            print(f"banknote {value} meets {count} times")

            action = int(input("""change the count ?
                1 - YES
                2 - NO
            """))

            match action:
                case 1:
                    while True:
                        try:
                            new_count_banknote = int(input("input new count: "))

                            if new_count_banknote < 0:
                                raise NegativeField("negative new count")
                            cash_machine[value] = new_count_banknote
                            change_cash_machine(cash_machine)
                            break

                        except InvalidAction as e:
                            print(str(e))
                            continue
                        except ValueError:
                            print("value must be number")
                            continue
                        except NegativeField as e:
                            print(str(e))
                            continue
                    break
                case 2:
                    break
                case _:
                    raise InvalidAction("a non-existent action is entered")


def add_user_db(name_argument, password_argument):
    with sql.connect("users.db") as connection:
        cursor = connection.cursor()
        balance = 0

        cursor.execute('INSERT INTO users (name, password, balance)'
                       ' values (?, ?, ?)',
                       (name_argument, password_argument, balance))


def create_user():
    while True:
        try:
            name = input("input username: ")
            password = input("input password: ")

            if create_validation(name, password):
                add_user_db(name, password)
                print("user has been added")
                get_command(user_command, name)
            break
        except InvalidUser as e:
            print(str(e))


def login():
    try:
        for attempt in range(1, 4):
            name = input("input username: ")
            password = input("input password: ")

            if is_admin(name, password):
                get_command(admin_panel, name)
            if login_validation(name, password) and not is_admin(name, password):
                get_command(user_command, name)
                break
            if not login_validation(name, password) and attempt == 3:
                raise InvalidUser("user or password are invalid")

    except InvalidUser as e:
        print(str(e))


def start():
    get_command(start_command)


start()
