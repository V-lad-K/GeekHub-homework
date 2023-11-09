# Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї
# функції. Тобто щоб її можна було використати у вигляді:
#     for i in my_range(1, 10, 2):
#         print(i)
#     1
#     3
#     5
#     7
#     9
#    P.S. Повинен вертатись генератор.
#    P.P.S. Для повного розуміння цієї функції - можна почитати
#    документацію по ній:
#    https://docs.python.org/3/library/stdtypes.html#range
#    P.P.P.S Не забудьте обробляти невалідні ситуації
#    (аналог range(1, -10, 5)). Подивіться як веде себе стандартний range в таких випадках.

class InvalidGenerator(Exception):
    pass


def range_generator(*args):
    length_args = len(args)

    match length_args:
        case 1:
            start = 0
            stop = args[0]
            step = 1
        case 2:
            start = args[0]
            stop = args[1]
            step = 1
        case 3:
            start = args[0]
            stop = args[1]
            step = args[2]
            if step == 0:
                raise InvalidGenerator("step must not be zero")
        case _:
            raise InvalidGenerator("0 arguments")

    if step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step


try:
    for item in range_generator(1, 0):
        print(item)
except InvalidGenerator as e:
    print(str(e))
except ValueError as e:
    print("arguments must be int")
