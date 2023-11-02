# Написати функцію <bank> , яка працює за наступною логікою: користувач
# робить вклад у розмірі <a> одиниць строком на <years> років під
# <percents> відсотків (кожен рік сума вкладу збільшується на цей
# відсоток, ці гроші додаються до суми вкладу і в наступному році на
# них також нараховуються відсотки).Параметр <percents>є необов'язковим
# і має значення по замовчуванню <10> (10%). Функція повинна принтануть
# суму, яка буде на рахунку, а також її повернути (але округлену до копійок).

class NegativeArguments(Exception):
    pass


def bank(deposit_argument, years_argument, percent_argument=0.1):
    for i in range(years_argument):
        deposit_argument += deposit_argument*percent_argument

    return round(deposit_argument, 2)


try:
    deposit = float(input("input deposit "))
    years = int(input("input number of years "))
    percent = float(input("input percent ")) / 100

    if deposit < 0 or years < 0 or percent < 0:
        raise NegativeArguments
    print(bank(deposit, years, percent))
except ValueError:
    print("deposit and years must be numbers")
except NegativeArguments:
    print("deposit and years must be positive")
