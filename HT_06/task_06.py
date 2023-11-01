# Написати функцію, яка буде реалізувати логіку циклічного зсуву
# елементів в списку. Тобто функція приймає два аргументи: список і
# величину зсуву (якщо ця величина додатня - пересуваємо з кінця на
# початок, якщо від'ємна - навпаки - пересуваємо елементи з початку
# списку в його кінець).
#    Наприклад:
#    fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
#    fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]

def shifter(list_argument, shift):
    if shift > 0:
        length = len(list_argument)

        return list_argument[length - shift:] + list_argument[:length - shift]
    elif shift < 0:
        return list_argument[shift:] + list_argument[:shift]
    else:
        return list_argument


print(shifter([1, 2, 3, 4, 5], 1))
