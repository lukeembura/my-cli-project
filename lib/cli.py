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