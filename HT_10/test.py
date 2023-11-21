import sqlite3 as sql


conn = sql.connect("users.db")


def create_users():
    with conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                name TEXT,
                password TEXT,
                balance INTEGER,
                is_admin BOOL,
                user_id INTEGER PRIMARY KEY AUTOINCREMENT
            )
        """)


def add_user(name, password, balance, is_admin):
    with conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (name, password, balance, is_admin)
            VALUES  (?, ?, ?, ?)
        """, (name, password, balance, is_admin))


def delete_transactions():
    with conn:
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM transactions
        """)


delete_transactions()
# add_user("admin", "admin", 0, True)
