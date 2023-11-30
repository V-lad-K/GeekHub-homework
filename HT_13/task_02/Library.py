# Створіть за допомогою класів та продемонструйте свою реалізацію
# шкільної бібліотеки (включіть фантазію). Наприклад вона може містити
# класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.

from exceptions import (
    InvalidUser,
    InvalidAction
)

from validations import Validation
from database import Database
from User import User

class Library:
    def __init__(self):
        self.validation = Validation()
        self.databese = Database()

    @staticmethod
    def get_command(func, *args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
                break
            except InvalidAction as e:
                print(str(e))
                continue
            except InvalidUser as e:
                print(str(e))
                continue

    def login(self):
        try:
            for attempt in range(3):
                name = input("input username: ")
                password = input("input password: ")
                user = User(name, password)
                if not self.validation.login_validation(name, password):
                    print("user is not exist")
                    continue
                else:
                    self.get_command(self.user_command, user)
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
                user = User(name, password)
                if self.validation.create_user_validation(name, password):
                    self.databese.add_user_db(name, password)
                    print("user has been added")
                    self.get_command(self.user_command, user)
                    break
            except InvalidUser as e:
                print(str(e))
                if count == 3:
                    break

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

    def user_command(self, user):
        while True:
            action = int(input("""Enter action  :
                               1. return book
                               2. take book
                               3. Exit
                           """))

            match action:
                case 1:
                    user.return_book_command()
                case 2:
                    user.take_book_command()
                case 3:
                    return
                case _:
                    raise InvalidAction("a non-existent action is entered")

    def start(self):
        self.get_command(self.start_command)


library = Library()
library.start()
