#  Створити клас Calc, який буде мати атребут last_result та 4 методи.
#  Методи повинні виконувати математичні операції з 2-ма числами, а
#  саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута
# last_result він повинен повернути пусте значення. Якщо використати
# один з методів - last_result повенен повернути результат виконання
# ПОПЕРЕДНЬОГО методу.
#     Example:
#     last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6

class ZeroDivision(Exception):
    pass


class Calc:
    """
        a class that performs calculations and calculates
        a new last_result
    """
    def __init__(self):
        """initialization"""
        self.last_result = None
        self.result = None

    def addition(self, number_1, number_2):
        """
            returns the sum of two values
        """
        self.last_result = self.result
        self.result = number_1 + number_2
        return self.result

    def subtraction(self, number_1, number_2):
        """
            returns the difference between two values
        """
        self.last_result = self.result
        self.result = number_1 - number_2
        return self.result

    def multiplication(self, number_1, number_2):
        """
            returns the product of two values
        """
        self.last_result = self.result
        self.result = number_1 * number_2
        return self.result

    def division(self, number_1, number_2):
        """
            returns the division of two values
        """

        if number_2 == 0:
            raise ZeroDivision("division on 0")

        self.last_result = self.result
        self.result = number_1 / number_2
        return self.result


try:
    calc = Calc()

    print(calc.addition(1, 2))
    print("last_result:", calc.last_result)

    print(calc.subtraction(3, 4))
    print("last_result:", calc.last_result)

    print(calc.division(5, 6))
    print("last_result:", calc.last_result)

    print(calc.multiplication(7, 8))
    print("last_result:", calc.last_result)

    print(calc.multiplication(7, 8))
    print("last_result:", calc.last_result)
except ZeroDivision as e:
    print(str(e))
except ValueError as e:
    print("value must be numbers")
