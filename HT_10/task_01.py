# Банкомат 2.0
#     - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких
#     файлів. Якщо в попередньому завданні ви добре продумали структуру
#     програми то у вас не виникне проблем швидко адаптувати її до нових
#     вимог.
#     - на старті додати можливість залогінитися або створити новго
#     користувача (при створенні новго користувача, перевіряється
#     відповідність логіну і паролю мінімальним вимогам. Для перевірки
#     створіть окремі функції)
#     - в таблиці (базі) з користувачами має бути створений унікальний
#     користувач-інкасатор, який матиме розширені можливості (домовимось
#     , що логін/пароль будуть admin/admin щоб нам було простіше
#     перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20,
#     50, 100, 200, 500, 1000
#     - змінювати вручну кількість купюр або подивитися їх залишок в
#     банкоматі може лише інкасатор
#     - користувач через банкомат може покласти на рахунок лише сумму
#     кратну мінімальному номіналу що підтримує банкомат. В іншому
#     випадку - повернути "здачу" (наприклад при поклажі 1005 -->
#     повернути 5). Але це не має впливати на баланс/кількість купюр
#     банкомату, лише збільшуєтсья баланс користувача (моделюємо
#     наявність двох незалежних касет в банкоматі - одна на прийом,
#     інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є
#     всього в банкоматі.
#     - при неможливості виконання якоїсь операції - вивести
#   повідомлення з причиною (не вірний логін/пароль, недостатньо коштів
#   на раунку, неможливо видати суму наявними купюрами тощо.)

import sqlite3 as sql

from database import (
    add_user_db,
    get_cash_machine,
    get_user_balance,
    get_minimum_denomination,
    set_user_balance,
    change_cash_machine
)

from exceptions import (
    InvalidUser,
    NegativeBalance,
    InvalidAction,
    NegativeField
)

from validations import (
    login_validation,
    is_admin,
    create_user_validation
)

connection = sql.connect("users.db")


def replenish_balance(name):
    deposit_amount = float(input("input the amount you want to deposit: "))
    minimum_denomination = get_minimum_denomination()
    rest = deposit_amount % minimum_denomination

    if deposit_amount < 0:
        raise NegativeField("replenishment amount must be positive")
    if rest != 0:
        print("take the rest of ", rest)

    balance = get_user_balance(name)
    new_balance = str(balance + deposit_amount - rest)
    set_user_balance(name, "replenishment", deposit_amount, new_balance)


def take_balance(name):
    amount = float(input("input the amount you want to take: "))
    balance = get_user_balance(name)
    get_money = 0
    cash_machine = get_cash_machine()

    if amount < 0:
        raise NegativeField("withdrawal amount must be positive")
    if amount > balance:
        raise NegativeBalance("withdrawal amount must be < then balance")

    for i in cash_machine:
        while amount >= i:
            if cash_machine[i] == 0:
                break
            get_money += i
            amount -= i
            cash_machine[i] -= 1

    if amount == 0:
        new_balance = balance - get_money
        change_cash_machine(cash_machine)
        set_user_balance(name, "withdrawalad", get_money, new_balance)
    else:
        raise InvalidAction("cash_machine has not enough money or banknotes")


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
                    print("a non-existent action is entered")
                    # raise InvalidAction("a non-existent action is entered")


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
        action = int(input("""Enter action  :
                               1. Check the balance
                               2. Top up the balance
                               3. Withdraw money
                               4. Exit
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
                return
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
            return
        case _:
            raise InvalidAction("a non-existent action is entered")


def login():
    try:
        for attempt in range(1, 4):
            name = input("input username: ")
            password = input("input password: ")

            if is_admin(name):
                get_command(admin_panel, name)
                break
            if login_validation(name, password) and not is_admin(name):
                get_command(user_command, name)
                break
            if not login_validation(name, password) and attempt == 3:
                raise InvalidUser("user or password are invalid")

    except InvalidUser as e:
        print(str(e))


def create_user():
    while True:
        try:
            name = input("input username: ")
            password = input("input password: ")

            if create_user_validation(name, password):
                add_user_db(name, password)
                print("user has been added")
                get_command(user_command, name)
            break
        except InvalidUser as e:
            print(str(e))


def start():
    get_command(start_command)


start()
