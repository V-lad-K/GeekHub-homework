# Написати функцію, яка приймає на вхід список (через кому), підраховує
# кількість однакових елементів у ньомy і виводить результат.
# Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
# 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2,
# [1, 2] -> 2, True -> 1"


def get_identical_element(list_argument):
    list_argument = [str(item) if not isinstance(item, (bool, type(None)))
                     else item for item in list_argument]

    new_dict = {}
    new_dict = {char: list_argument.count(char)
                for char in list_argument if char not in new_dict}

    result = ', '.join(f"{key} ----> {value}" for key, value in new_dict.items())
    return result


print(get_identical_element([1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]))
