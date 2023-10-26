# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float, а якщо і там
# ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання для цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить відповідне
# повідомлення

def get_result(number1, number2, value_type: type):
    print(value_type(number1) / value_type(number2))


while True:
    value1 = input("input value1 ")
    value2 = input("input value2 ")
    try:
        get_result(value1, value2, int)
        break
    except ValueError:
        try:
            get_result(value1, value2, float)
            break
        except ValueError:
            print("input numbers again")
            continue
        except ZeroDivisionError:
            print("delete on 0")
    except ZeroDivisionError:
        print("delete on 0")
