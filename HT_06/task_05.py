# Написати функцію <fibonacci>,яка приймає один аргумент і виводить всі
# числа Фібоначчі, що не перевищують його.

def fibonacci(number_argument):
    fibonacci_list = []
    position_1, position_2 = 0, 1

    while position_1 <= number_argument:
        fibonacci_list.append(position_1)
        position_1, position_2 = position_2, position_1 + position_2
    return fibonacci_list


try:
    number = int(input("input number "))
    print(fibonacci(number))
except ValueError:
    print("number must be integer")
