# Створіть функцію, всередині якої будуть записано список із п'яти
# користувачів (ім'я та пароль). Функція повинна приймати три аргументи
# два - обов'язкових (<username> та <password>) і третій -
# необов'язковий параметр <silent> (значення за замовчуванням -<False>)
# Логіка наступна:
#     якщо введено коректну пару ім'я/пароль - вертається True;
#     якщо введено неправильну пару ім'я/пароль:
#         якщо silent == True - функція вертає False
#         якщо silent == False -породжується виключення LoginException
#         (його також треба створити =))

class LoginException(Exception):
    pass


def is_user(username, password, silent=False):
    for user in users:
        if username == user["username"] and password == user["password"]:
            return True

    if silent:
        return False
    else:
        raise LoginException


users = [
    {"username": "username1", "password": "password1"},
    {"username": "username2", "password": "password2"},
    {"username": "username3", "password": "password3"},
    {"username": "username4", "password": "password4"},
    {"username": "username5", "password": "password5"},
]


try:
    input_username = input("input name of user ")
    input_password = input("input password of user ")

    print(is_user(input_username, input_password))
except LoginException:
    print("username or password does not match")
