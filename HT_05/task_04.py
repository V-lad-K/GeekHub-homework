# Наприклад маємо рядок -->
# "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00ko7k5j78p3kj546p4
# просто потицяв по клавi =) Створіть ф-цiю, яка буде отримувати рядки
# на зразок цього та яка оброблює наступні випадки: -  якщо довжина
# рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка,
# кiлькiсть букв та цифр -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами
# (без пробілів) -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)

def get_sum(string_argument):
    new_string = "".join([" " if char.isalpha() else char
                          for char in string_argument])
    new_list = list(map(int, " ".join(new_string.split()).split()))
    return sum(list(filter(lambda x: x > 9, new_list)))


def get_result(string_argument):
    if 30 <= len(string_argument) <= 50:
        count = len([char for char in string_argument if char.isdigit()])

        print("length of string is", len(string_argument))
        print("count of letter is ", len(list(filter(lambda x: x.isalpha(),
                                                     string_argument))))
        print("count of digits is ", count)
    elif len(string_argument) < 30:
        print("count of digits is ", get_sum(string_argument))
        print("string without digits", "".join(filter(lambda x: x.isalpha(),
                                                      string_argument)))
    else:
        new_dict = {}
        new_dict = {char: string_argument.count(char)
                    for char in string_argument if char not in new_dict}
        print("umber of repetitions of each character ", new_dict)


string = "f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe0035po6j345h5vvghv5g"

get_result(string)
