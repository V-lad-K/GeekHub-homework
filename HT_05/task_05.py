# Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1
# ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку
# зробити! Аргументи брати від юзера (можна по одному - 2, окремо +,
# окремо 2; можна всі разом - типу 1 + 2). Операції що мають бути
# присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними
# значеннями на предмет помилок!

def calculator(number1, operation, number2):
    try:
        match operation:
            case "+":
                return number1 + number2
            case "-":
                return number1 - number2
            case "*":
                return number1 * number2
            case "/":
                return number1 / number2
            case "%":
                return number1 % number2
            case "//":
                return number1 // number2
            case "**":
                return number1 ** number2
            case _:
                return "operator not found"
    except ValueError:
        return "operands is not digits"
    except ZeroDivisionError:
        return "division on 0 "


operand_1 = float(input("input operand1 "))
operand_2 = float(input("input operand2 "))
operator = input("input operator: +, -, *, /, %, //, ** ")

print(calculator(operand_1, operator, operand_2))
