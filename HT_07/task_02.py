# Створіть функцію для валідації пари ім'я/пароль за наступними
# правилами:
#    - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#    - пароль повинен бути не меншим за 8 символів і повинен мати хоча
#    б одну цифру;
#    - пароль повинен мати хоча б одну велику літеру
#    Якщо якийсь із параментів не відповідає вимогам - породити
#    виключення із відповідним текстом.

class InvalidValidation(Exception):
    pass


def validation(username, password_argument):
    is_digit = any(char.isdigit() for char in password_argument)
    is_upper_case = any(char.isupper() for char in password_argument)

    if not 3 <= len(username) <= 50:
        raise InvalidValidation("username not in range 3 - 50")
    if not is_digit:
        raise InvalidValidation("password has not digit")
    if not is_upper_case:
        raise InvalidValidation("password has not capital symbol")
    if not len(password_argument) >= 8:
        raise InvalidValidation("password must be more than 8 symbols")

    return True


try:
    input_username = input("input name of user ")
    input_password = input("input password of user ")

    if validation(input_username, input_password):
        print("username and password are correct")

except InvalidValidation as e:
    print(str(e))
