# Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна
# повертати якийсь результат (напр. інпут від юзера, результат
# математичної операції тощо). Також створiть четверту ф-цiю, яка
# всередині викликає 3 попереднi,
# обробляє їх результат та також повертає результат своєї роботи. Таким
# чином ми будемо викликати одну (четверту) функцiю, а вона в своєму
# тiлi - ще 3.


def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def general(number1, number2):
    return (addition(number1, number2) + subtraction(number1, number2)
            + multiplication(number1, number2))


print(general(5, 10))
