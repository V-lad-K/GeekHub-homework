import sqlite3 as sql

from exceptions import InvalidUser
connection = sql.connect("users.db")


def get_users():
    with connection:
        cursor = connection.execute('SELECT * FROM users')
        users = cursor.fetchall()
        users_list = [{i[0]: i[1] for i in users}]

        return users_list


def get_user_by_id(name):
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT user_id
            FROM users
            WHERE name = ?
        """, (name,))
        return cursor.fetchone()[0]


def login_validation(name_argument, password_argument):
    users = get_users()

    return any(user.get(name_argument) == password_argument for user in users)


def is_admin(name_argument):
    user_id = get_user_by_id(name_argument)

    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT is_admin
            FROM users
            WHERE user_id = ?
        """, (user_id,))

        return cursor.fetchone()[0]


def create_user_validation(name_argument, password_argument):
    length_name = len(name_argument)
    length_password = len(password_argument)

    is_digit = any(char.isdigit() for char in password_argument)
    is_upper_case = any(char.isupper() for char in password_argument)

    if not 3 <= length_name <= 20:
        raise InvalidUser("user name must be in range 3 - 20")
    if not length_password >= 8:
        raise InvalidUser("user password must be more 8 symbols")
    if not is_digit:
        raise InvalidUser("password has not digit")
    if not is_upper_case:
        raise InvalidUser("password has not upper symbol")
    if login_validation(name_argument, password_argument):
        raise InvalidUser("user has been exists")
    return True
