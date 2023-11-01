# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0
# до 1000, и яка вертатиме True, якщо це число просте і False - якщо ні

class InvalidRange(Exception):
    pass


def is_prime(number_argument):
    if number_argument <= 1:
        return False

    for i in range(2, number_argument):
        if number_argument % i == 0:
            return False
    return True


try:
    number = int(input("input int number "))
    if not 0 <= number <= 1000:
        raise InvalidRange
    print(is_prime(25))
except ValueError:
    print("number must be integer")
except InvalidRange:
    print("out of range 0 - 1000")
