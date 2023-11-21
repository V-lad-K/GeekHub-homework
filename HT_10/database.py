import sqlite3 as sql

from validations import get_user_by_id

connection = sql.connect("users.db")


def get_cash_machine():
    with connection:
        cursor = connection.execute('SELECT value, count FROM cash_machine')
        users = cursor.fetchall()

        cash_machine = {i[0]: i[1] for i in users}

        return cash_machine


def change_cash_machine(machine):
    with connection:
        cursor = connection.cursor()

        for key, value in machine.items():
            cursor.execute("""
                UPDATE cash_machine
                SET count = ?
                WHERE value = ?
            """, (value, key))


def get_user_balance(name):
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT balance 
            FROM users
            WHERE name == ?
        """, (name,))
        connection.commit()

        return cursor.fetchone()[0]


def set_user_balance(name, type_operation, amount, balance):
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE users
            SET balance = ?
            WHERE name = ?
        """, (balance, name))

    set_transaction(name, type_operation, amount)


def set_transaction(name, type_operation, amount):
    user_id = get_user_by_id(name)

    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO transactions (type, total, user_id)
            VALUES (?, ?, ?)
        """, (type_operation, amount, user_id))


def get_minimum_denomination():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT value
            FROM cash_machine
        """)

        minimum_denomination = min(cursor.fetchall())

        return minimum_denomination[0]


def add_user_db(name_argument, password_argument):
    with connection:
        cursor = connection.cursor()
        balance = 0
        admin_user = False

        cursor.execute('INSERT INTO users (name, password, balance, is_admin)'
                       ' values (?, ?, ?, ?)',
                       (name_argument, password_argument, balance, admin_user))
