# Написати функцію <fibonacci>,яка приймає один аргумент і виводить всі
# числа Фібоначчі, що не перевищують його.

def is_fibonacci(number_argument):
    if number_argument == 1:
        return 0
    if number_argument == 2:
        return 1
    return is_fibonacci(number_argument - 1) + is_fibonacci(number_argument - 2)


def fibonacci(number_argument):
    new_list = []

    for item in range(1, number_argument+1):
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
