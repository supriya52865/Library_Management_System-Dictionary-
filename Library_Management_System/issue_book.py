from utils import books, issue_books

def issue():
    book_id = input("Enter Book ID: ")

    if book_id in books:
        issue_books[book_id] = books[book_id]
        del books[book_id]

        print("Book assigned successfully")
    else:
        print("Book not available")