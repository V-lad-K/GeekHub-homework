# Написати функцію <square>, яка прийматиме один аргумент - сторону
# квадрата, і вертатиме 3 значення у вигляді кортежа: периметр квадрата
# площа квадрата та його діагональ.

import math


class NegativeSide(Exception):
    pass


def square_perimetr(square_side):
    return 4*square_side


def square_area(square_side):
    return square_side ** 2


def square_diagonal(square_side):
    return math.sqrt(2) * square_side


def square(square_side):
    return (square_perimetr(square_side), square_area(square_side),
            square_diagonal(square_side))


try:
    side = float(input("input side of square "))
    if side < 0:
        raise NegativeSide
    print(square(side))
except ValueError:
    print("side must be number")
except NegativeSide:
    print("side must be positive")
