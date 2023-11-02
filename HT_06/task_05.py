# Написати функцію <fibonacci>,яка приймає один аргумент і виводить всі
# числа Фібоначчі, що не перевищують його.

def is_fibonacci(number_argument):
    position_1 = 1
    position_2 = 1

    if number_argument == 0:
        return 0
    if number_argument == 1:
        return 1

    for i in range(2, number_argument):
        position_1, position_2 = position_2, position_1 + position_2

    return position_2


def fibonacci(number_argument):
    new_list = []

    for item in range(number_argument+1):
        if number_argument > is_fibonacci(item):
            new_list.append(is_fibonacci(item))
        else:
            break

    return new_list


try:
    number = int(input("input number "))
    print(fibonacci(number))
except ValueError:
    print("number must be integer")
