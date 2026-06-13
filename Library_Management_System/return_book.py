from utils import issue_books, books

def return_book():
    book_id = input("Enter Book ID: ")

    if book_id in issue_books:
        books[book_id] = issue_books[book_id]
        del issue_books[book_id]

        print("Book returned successfully")
    else:
        print("Book was not issued")