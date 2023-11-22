# Створити клас Person, в якому буде присутнім метод __init__ який буде
# приймати якісь аргументи, які зберігатиме в відповідні змінні. Методи,
# які повинні бути в класі Person - show_age, print_name,
# show_all_information. Створіть 2 екземпляри класу Person та в кожному
# з екземплярів створіть атребут profession (його не має інсувати під час ініціалізації).

class InvalidName(Exception):
    pass


class InvalidAge(Exception):
    pass


class Person:
    def __init__(self, name: str, age: float):
        if not name:
            raise InvalidName("name is empty")
        if not isinstance(name, str):
            raise InvalidName("name is not string")
        if age < 0:
            raise InvalidName("age must be positive")
        if not isinstance(age, (float, int)):
            print(type(age))
            raise InvalidName("age must be number")

        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    def show_all_information(self):
        print(self.__dict__)


try:
    person1 = Person("Vlad", 21)
    person1.show_all_information()
    person1.profession = "developer"
    person1.show_all_information()

    person2 = Person("Nika", 22.0)
    person2.show_all_information()
    person2.profession = "teacher"
    person2.show_all_information()
except InvalidName as e:
    print(str(e))
except InvalidAge as e:
    print(str(e))
