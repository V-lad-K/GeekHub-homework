import sqlite3 as sql
connection = sql.connect("library")


def create_authors():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS author (
                name TEXT NOT NULL,
                age INTEGET,
                author_id INTEGER PRIMARY KEY AUTOINCREMENT
            )
            
        """)


def add_authors(name, age):
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO author (name, age)
            VALUES (?, ?)
        """, (name, age))


def create_book():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS book (
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                author_id INTEGER,
                category_id INTEGER,
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                FOREIGN KEY (category_id) REFERENCES category(category_id),
                FOREIGN KEY (author_id) REFERENCES author(author_id)
            )
        """)


def add_book(name, description, author_id, category_id):
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
                INSERT INTO book (name, description, author_id, category_id)
                VALUES (?, ?, ?, ?)
            """, (name, description, author_id, category_id))


def create_category():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categoty (
                name TEXT NOT NULL,
                category_id INTEGER PRIMARY KEY AUTOINCREMENT
            )
            
        """)


def add_category(name):
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO categoty (name)
            VALUES (?)
        """, (name, ))


def create_user():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                name TEXT NOT NULL,
                password TEXT NOT NULL, 
                user_id INTEGER PRIMARY KEY AUTOINCREMENT
                
            )
            
        """)


def delete_users():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
                DELETE FROM users
                
            """)


def delete_report():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
                DELETE FROM report
                
            """)


def add_user_db(name_argument, password_argument):
    with connection:
        print("add_user_db")
        cursor = connection.cursor()

        cursor.execute('INSERT INTO users (name, password)'
                       ' values (?, ?)',
                       (name_argument, password_argument))


def create_report():
    with connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS report (
                user_id INTEGER,
                book_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (book_id) REFERENCES book(book_id)
            )
        """)


def add_report():
    with connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO report (user_id, book_id)'
                       ' values (?, ?)',
                       (1, 2))


add_user_db("Vlad", "Vlad123123")
delete_users()
