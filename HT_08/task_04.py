# Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну
# послідовність (рядок, список, кортеж) і повертає генератор, який буде
# вертати значення з цієї послідовності, при цьому, якщо було повернено
# останній елемент із послідовності - ітерація починається знову.
#    Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
#    for elem in generator([1, 2, 3]):
#        print(elem)
#    1
#    2
#    3
#    1
#    2
#    3
#    1

def range_generator(iterable):
    if not isinstance(iterable, (str, list, tuple)):
        raise ValueError

    while True:
        for _ in iterable:
            yield _


try:
    for item in range_generator([1, 2, 3]):
        print(item)
except ValueError:
    print("not iterable argument")
