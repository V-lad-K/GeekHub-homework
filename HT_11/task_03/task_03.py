# Банкомат 2.0: переробіть программу з функціонального підходу
# програмування на використання класів. Додайте шанс 10% отримати бонус
# на баланс при створенні нового користувача.

from database import Database
from exceptions import (InvalidUser,
                        NegativeBalance,
                        InvalidAction,
                        NegativeField)

from validations import Validation


class CashMachine:
    def __init__(self):
        self.databese = Database()
        self.validation = Validation()

    def replenish_balance(self, name):
        deposit_amount = float(input("input the amount you want to deposit: "))
        minimum_denomination = self.databese.get_minimum_denomination()
        rest = deposit_amount % minimum_denomination

        if deposit_amount < 0:
            raise NegativeField("replenishment amount must be positive")
        if rest != 0:
            print("take the rest of ", rest)

        balance = self.databese.get_user_balance(name)
        new_balance = str(balance + deposit_amount - rest)
        self.databese.set_user_balance(name, "replenishment", deposit_amount,
                                       new_balance)

    def take_balance(self, name):
        amount = float(input("input the amount you want to take: "))
        balance = self.databese.get_user_balance(name)
        get_money = 0
        cash_machine = self.databese.get_cash_machine()

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
            self.databese.change_cash_machine(cash_machine)
            self.databese.set_user_balance(name, "withdrawalad", get_money,
                                           new_balance)
        else:
            raise InvalidAction("cash_machine has not enough money or banknotes")

    def change_number_banknote(self):
        cash_machine = self.databese.get_cash_machine()

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
                                self.databese.change_cash_machine(cash_machine)
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

    @staticmethod
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

    def user_command(self, name):
        while True:
            action = int(input("""Enter action  :
                               1. Check the balance
                               2. Top up the balance
                               3. Withdraw money
                               4. Exit
                           """))

            match action:
                case 1:
                    print(self.databese.get_user_balance(name))
                case 2:
                    self.replenish_balance(name)
                case 3:
                    self.take_balance(name)
                case 4:
                    return
                case _:
                    raise InvalidAction("a non-existent action is entered")

    def admin_command(self):
        while True:
            action = int(input("""input action
                        1 - to see cash machine balance
                        2 - change number of banknotes
                        3 - exit
                    """))

            match action:
                case 1:
                    print(self.databese.get_cash_machine())
                case 2:
                    self.change_number_banknote()
                case 3:
                    return
                case _:
                    raise InvalidAction("a non-existent action is entered")

    def start_command(self):
        while True:
            choice = int(input(""" input action
                1 - log in
                2 - registration
                3 - exit
            """))

            match choice:
                case 1:
                    self.login()
                case 2:
                    self.create_user()
                case 3:
                    break
                case _:
                    raise InvalidAction("a non-existent action is entered")

    def admin_panel(self, name):
        action = int(input(""" input action
                    1 - log in as a collector
                    2 - log in as a user
                    3 - exit
                """))

        match action:
            case 1:
                self.get_command(self.admin_command)
            case 2:
                self.get_command(self.user_command, name)
            case 3:
                return
            case _:
                raise InvalidAction("a non-existent action is entered")

    def login(self):
        try:
            for attempt in range(3):
                name = input("input username: ")
                password = input("input password: ")

                if not self.validation.login_validation(name, password):
                    print("user is not exist")
                    continue
                if self.validation.is_admin(name):
                    self.get_command(self.admin_panel, name)
                    break
                if (self.validation.login_validation(name, password)
                        and not self.validation.is_admin(name)):
                    self.get_command(self.user_command, name)
                    break

        except InvalidUser as e:
            print(str(e))

    def create_user(self):
        count = 0
        while True:
            count += 1
            try:
                name = input("input username: ")
                password = input("input password: ")

                if self.validation.create_user_validation(name, password):
                    self.databese.add_user_db(name, password)
                    print("user has been added")
                    self.get_command(self.user_command, name)
                    break
            except InvalidUser as e:
                print(str(e))
                if count == 3:
                    break

    def start(self):
        self.get_command(self.start_command)


machine = CashMachine()
machine.start()
