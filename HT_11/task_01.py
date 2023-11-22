class ZeroDivision(Exception):
    pass


class Calc:
    def __init__(self):
        self.last_result = None
        self.results = [None]

    def addition(self, number_1, number_2):
        addition_result = number_1 + number_2
        self.set_last_result(addition_result)
        return addition_result

    def subtraction(self, number_1, number_2):
        subtraction_result = number_1 - number_2
        self.set_last_result(subtraction_result)
        return subtraction_result

    def multiplication(self, number_1, number_2):
        multiplication_result = number_1 * number_2
        self.set_last_result(multiplication_result)
        return multiplication_result

    def division(self, number_1, number_2):
        if number_2 == 0:
            raise ZeroDivision("division on 0")
        division_result = number_1 / number_2
        self.set_last_result(division_result)
        return division_result

    def set_last_result(self, result):
        self.results.append(result)
        self.last_result = self.results[-2]
        print("self.last_result", self.last_result)


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
