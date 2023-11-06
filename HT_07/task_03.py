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
        raise InvalidValidation("password must be more than 8 symbols")
    if not len(password_argument) >= 8:
        raise InvalidValidation("password must be more than 8 symbols")

    return True


def print_result(username, password_argument, error="OK"):
    print("Name", username)
    print("Password", password_argument)
    print("Status", error)


users = [
    {"username": "Vlad", "password": "Vlad123123"},
    {"username": "Sasha", "password": "sasha123123"},
    {"username": "Iv", "password": "Iv123123"},
    {"username": "K", "password": "V"},
    {"username": "Maria", "password": "j"},
]

for user_dict in users:
    name = user_dict["username"]
    password = user_dict["password"]

    try:
        if validation(name, password):
            print_result(name, password)

    except InvalidValidation as e:
        print_result(name, password, str(e))
