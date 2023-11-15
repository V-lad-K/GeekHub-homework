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


import csv
import json


class InvalidUser(Exception):
    pass


class NegativeBalance(Exception):
    pass


class InvalidAction(Exception):
    pass


class NegativeField(Exception):
    pass


def get_users():
    with open("users.csv", "r") as f:
        reader = csv.DictReader(f)
        users = {user["name"]: user["password"] for user in reader}

        return users


def get_user_balance(name):
    with open(f"{name}_balance.txt", "r") as f:
        user_balance = float(f.read())
        return user_balance


def set_user_balance(name, type_operation, amount, balance):
    with open(f"{name}_balance.txt", "w") as f:
        f.write(balance)
    set_transaction(name, type_operation, amount, balance)


def get_transaction(name):
    try:
        with open(f"{name}_transactions.json", "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return []


def set_transaction(name, type_operation, amount, balance):
    transaction = get_transaction(name)

    with open(f"{name}_transactions.json", 'w') as f:
        transaction_dict = {
            "type": type_operation,
            "amount": amount,
            "balance": balance
        }
        transaction.append(transaction_dict)
        json.dump(transaction, f, indent=2)


def replenish_balance(name):
    deposit_amount = float(input("input the amount you want to deposit: "))
    if deposit_amount < 0:
        raise NegativeField("deposit_amount must be positive")

    balance = get_user_balance(name)
    new_balance = str(balance + deposit_amount)
    set_user_balance(name, "replenishment", deposit_amount, new_balance)


def take_balance(name):
    deposit_amount = float(input("input the amount you want to take: "))
    if deposit_amount < 0:
        raise NegativeField("deposit_amount must be positive")

    balance = get_user_balance(name)

    if deposit_amount > balance:
        raise NegativeBalance("deposit_amount must be < then balance")

    new_balance = str(balance - deposit_amount)
    set_user_balance(name, "withdrawal", deposit_amount, new_balance)


def get_command_action(name):
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
                break
            case _:
                raise InvalidAction("a non-existent action is entered")


def login_validation(name_argument, password_argument):
    users = get_users()

    return name_argument in users and password_argument == users[name_argument]


def start():
    try:
        for attempt in range(1, 4):
            name = input("input username: ")
            password = input("input password: ")

            if login_validation(name, password):
                get_command_action(name)
                break
            if not login_validation(name, password) and attempt == 3:
                raise InvalidUser("user or password are invalid")

    except InvalidUser as e:
        print(str(e))
        get_command_action(name)
    except NegativeBalance as e:
        print(str(e))
        get_command_action(name)
    except InvalidAction as e:
        print(str(e))
        get_command_action(name)
    except ValueError:
        print("value must be number")
        get_command_action(name)
    except NegativeField as e:
        print(str(e))
        get_command_action(name)


start()
