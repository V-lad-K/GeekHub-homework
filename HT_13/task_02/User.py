from validations import Validation
from database import Database


class User:
    def __init__(self, name, password):
        self.validation = Validation()
        self.databese = Database()
        self.name = name
        self.password = password

    def take_book_command(self):
        print(f"list of all free books: {self.databese.get_available_books()}")

        take_book_choice = input("""input the book you want to take
            or write nothing: 
        """)
        if take_book_choice in self.databese.get_available_books():
            user_id = self.databese.get_user_id(self.name)
            book_id = self.databese.get_book_id(take_book_choice)
            self.databese.set_report(user_id, book_id)

    def return_book_command(self):
        user_id = self.databese.get_user_id(self.name)
        print(f"""a list of all the books that were taken:
            {self.databese.get_books_by_user(user_id)}
        """)
        take_book_choice = input("""input the book what you want to return
            or write nothing: 
        """)
        if take_book_choice in self.databese.get_books_by_user(user_id):
            book_id = self.databese.get_book_id(take_book_choice)
            self.databese.delete_report(user_id, book_id)
