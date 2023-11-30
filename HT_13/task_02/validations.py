import sqlite3 as sql

from exceptions import InvalidUser
connection = sql.connect("library")


class Validation:
    @staticmethod
    def get_users():
        with connection:
            cursor = connection.execute('SELECT * FROM users')
            users = cursor.fetchall()
            users_list = [{i[0]: i[1] for i in users}]

            return users_list

    @staticmethod
    def get_user_by_id(name):
        with connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT user_id
                FROM users
                WHERE name = ?
            """, (name,))
            return cursor.fetchone()[0]

    def login_validation(self, name_argument, password_argument):
        users = self.get_users()
        return any(user.get(name_argument) == password_argument
                   for user in users)

    @staticmethod
    def create_user_validation(name_argument, password_argument):
        length_name = len(name_argument)
        is_digit = any(char.isdigit() for char in password_argument)

        if not 3 <= length_name <= 20:
            raise InvalidUser("user name must be in range 3 - 20")
        if not is_digit:
            raise InvalidUser("password has not digit")
        return True
