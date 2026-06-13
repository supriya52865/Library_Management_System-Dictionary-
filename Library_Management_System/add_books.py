from utils import books

def add():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ").upper()

    books[book_id] = {
        "name": book_name
    }

    print(f"Book Added: {book_name}")