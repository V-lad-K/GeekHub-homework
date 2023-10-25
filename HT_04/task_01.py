# Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
# Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float, а якщо і там
# ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання для цього використати цикл while)
# Виводить результат ділення першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить відповідне
# повідомлення

while True:
    value1 = input("input value1 ")
    value2 = input("input value2 ")

    try:
        value1 = float(value1)
        value2 = float(value2)
        result = value1/value2
        print(result)
        break
    except ValueError:
        print("input values again")
        continue
    except ZeroDivisionError as zde:
        print(str(zde))
        continue
