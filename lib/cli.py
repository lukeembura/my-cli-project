from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Author, Book

DATABASE_URL = "sqlite:///lib/db/library.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def main_menu():
    while True:
        print("\nLibrary CLI")
        print("1. Manage Authors")
        print("2. Manage Books")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            author_menu()
        elif choice == '2':
            book_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def author_menu():
    while True:
        print("\nAuthor Menu")
        print("1. List all authors")
        print("2. Create author")
        print("3. Delete author")
        print("4. Find author by ID")
        print("5. Back to main menu")
        choice = input("Choose an option: ")

        if choice == '1':
            authors = Author.get_all(session)
            for a in authors:
                print(f"{a.id}: {a.name}")
        elif choice == '2':
            name = input("Enter author name: ")
            author = Author.create(session, name)
            print(f"Created author with id {author.id}")
        elif choice == '3':
            author_id = int(input("Enter author ID to delete: "))
            author = Author.find_by_id(session, author_id)
            if author:
                author.delete(session)
                print("Author deleted.")
            else:
                print("Author not found.")
        elif choice == '4':
            author_id = int(input("Enter author ID to find: "))
            author = Author.find_by_id(session, author_id)
            if author:
                print(f"Author: {author.id} - {author.name}")
                print("Books:")
                for book in author.books:
                    print(f" - {book.title}")
            else:
                print("Author not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

def book_menu():
    while True:
        print("\nBook Menu")
        print("1. List all books")
        print("2. Create book")
        print("3. Delete book")
        print("4. Find book by ID")
        print("5. Back to main menu")
        choice = input("Choose an option: ")

        if choice == '1':
            books = Book.get_all(session)
            for b in books:
                print(f"{b.id}: {b.title} (Author: {b.author.name})")
        elif choice == '2':
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID for this book: "))
            author = Author.find_by_id(session, author_id)
            if author:
                book = Book.create(session, title, author_id)
                print(f"Created book with id {book.id}")
            else:
                print("Author not found. Cannot create book.")
        elif choice == '3':
            book_id = int(input("Enter book ID to delete: "))
            book = Book.find_by_id(session, book_id)
            if book:
                book.delete(session)
                print("Book deleted.")
            else:
                print("Book not found.")
        elif choice == '4':
            book_id = int(input("Enter book ID to find: "))
            book = Book.find_by_id(session, book_id)
            if book:
                print(f"Book: {book.id} - {book.title} (Author: {book.author.name})")
            else:
                print("Book not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again.")

    
if __name__ == "__main__":
    main_menu()