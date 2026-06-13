from utils import books

def show():
    if len(books) == 0:
        print("Book not available")
    else:
        print("\nAvailable Books:")
        for book_id, details in books.items():
            print(f"Book ID: {book_id}")
            print(f"Book Name: {details['name']}")
            print("-" * 20)