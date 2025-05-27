from lib.db.models import Author, Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lib/db/library.db')
Session = sessionmaker(bind=engine)
session = Session()

def menu():
    print("\nLibrary Manager")
    print("1. View all authors")
    print("2. View all books")
    print("3. Add a new author")
    print("4. Add a new book")
    print("5. Delete an author")
    print("6. Delete a book")
    print("7. Find author by ID")
    print("8. Find book by ID")
    print("9. View books by author")
    print("0. Exit")

def run():
    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            authors = Author.get_all(session)
            for a in authors:
                print(a)
        elif choice == "2":
            books = Book.get_all(session)
            for b in books:
                print(b)
        elif choice == "3":
            name = input("Enter author name: ")
            Author.create(session, name=name)
            print("Author added.")
        elif choice == "4":
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            try:
                Book.create(session, title=title, author_id=int(author_id))
                print("Book added.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "5":
            author_id = input("Enter author ID to delete: ")
            author = Author.find_by_id(session, int(author_id))
            if author:
                Author.delete(session, author)
                print("Author deleted.")
            else:
                print("Author not found.")
        elif choice == "6":
            book_id = input("Enter book ID to delete: ")
            book = Book.find_by_id(session, int(book_id))
            if book:
                Book.delete(session, book)
                print("Book deleted.")
            else:
                print("Book not found.")
        elif choice == "7":
            author_id = input("Enter author ID: ")
            author = Author.find_by_id(session, int(author_id))
            print(author if author else "Author not found.")
        elif choice == "8":
            book_id = input("Enter book ID: ")
            book = Book.find_by_id(session, int(book_id))
            print(book if book else "Book not found.")
        elif choice == "9":
            author_id = input("Enter author ID: ")
            author = Author.find_by_id(session, int(author_id))
            if author:
                for book in author.books:
                    print(book)
            else:
                print("Author not found.")
        elif choice == "0":
            print("Exiting CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    run()
