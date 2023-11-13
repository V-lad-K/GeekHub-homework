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


def my_range(start=0, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step > 0:
        while start < stop:
            print(start)
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        raise InvalidGenerator("step can't be 0")


try:
    for i in my_range(0, -10, -1):
        print(i)
except InvalidGenerator as e:
    print(str(e))
