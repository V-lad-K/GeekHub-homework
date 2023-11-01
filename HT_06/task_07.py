# Написати функцію, яка приймає на вхід список (через кому), підраховує
# кількість однакових елементів у ньомy і виводить результат.
# Елементами списку можуть бути дані будь-яких типів.
#     Наприклад:
# 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2,
# [1, 2] -> 2, True -> 1"

def get_identical_element(list_argument):
    list_argument = list(map(str, list_argument))
    new_dict = {}
    new_dict = {str(char): list_argument.count(char)
                for char in list_argument if str(char) not in new_dict}
    return "number of repetitions of each character ", new_dict


print(get_identical_element([1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]))
