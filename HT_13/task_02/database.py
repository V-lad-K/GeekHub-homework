import sqlite3 as sql
connection = sql.connect("library")


class Database:
    @staticmethod
    def add_user_db(name_argument, password_argument):
        with connection:
            cursor = connection.cursor()

            cursor.execute('INSERT INTO users (name, password)'
                           ' values (?, ?)',
                           (name_argument, password_argument))

    def get_available_books(self):
        all_books_list = self.get_all_book()
        not_available_books_list = self.get_books_id_from_report()
        available_books_list = list(set(all_books_list) - set(not_available_books_list))

        with connection:
            cursor = connection.cursor()
            query = '''
                SELECT name
                FROM book
                WHERE book_id IN ({seq})
            '''.format(seq=','.join(['?']*len(available_books_list)))

            cursor.execute(query, available_books_list)
            books = [book[0] for book in cursor.fetchall()]
            return books

    @staticmethod
    def get_books_id_from_report():
        with connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT book_id
                FROM report
            """)

            books_id_list = [item[0] for item in cursor.fetchall()]
            return books_id_list

    @staticmethod
    def get_books_by_user(user_id):
        with connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT book_id
                FROM report
                WHERE report.user_id = ?
            """, (user_id,))

            books_id_list = [item[0] for item in cursor.fetchall()]
            query = '''
                SELECT name
                FROM book
                WHERE book_id IN ({seq})
            '''.format(seq=','.join(['?']*len(books_id_list)))

            cursor.execute(query, books_id_list)
            books = [book[0] for book in cursor.fetchall()]
            return books

    @staticmethod
    def get_all_book():
        with connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT book_id
                FROM book
            """)

            books_id_list = [item[0] for item in cursor.fetchall()]
            return books_id_list

    @staticmethod
    def get_book_id(name):
        with connection:
            cursor = connection.cursor()

            cursor.execute("""
                        SELECT book_id
                        FROM book
                        WHERE book.name = ?
                    """, (name, ))

            return cursor.fetchone()[0]

    @staticmethod
    def set_report(user_id, book_id):
        with connection:
            cursor = connection.cursor()

            cursor.execute('INSERT INTO report (user_id, book_id)'
                           ' values (?, ?)',
                           (user_id, book_id))

    @staticmethod
    def delete_report(user_id, book_id):
        with connection:
            cursor = connection.cursor()

            cursor.execute("""
                DELETE FROM report
                WHERE user_id = ? AND book_id = ?
            """, (user_id, book_id))

    @staticmethod
    def get_user_id(name):
        with connection:
            cursor = connection.cursor()

            cursor.execute("""
            SELECT user_id
            FROM users
            WHERE name = ?
        """, (name,))

            return cursor.fetchone()[0]
