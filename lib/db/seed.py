from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Author, Book

# Create the database engine
engine = create_engine('sqlite:///lib/db/library.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop and recreate all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Seed Authors
author1 = Author.create(session, name="Chinua Achebe")
author2 = Author.create(session, name="Ngũgĩ wa Thiong'o")
author3 = Author.create(session, name="Margaret Ogola")
author4 = Author.create(session, name="Wole Soyinka")

# Seed Books
Book.create(session, title="Things Fall Apart", author_id=author1.id)
Book.create(session, title="No Longer at Ease", author_id=author1.id)
Book.create(session, title="The River Between", author_id=author2.id)
Book.create(session, title="Weep Not, Child", author_id=author2.id)
Book.create(session, title="The River and the Source", author_id=author3.id)

try:
    author_id = int(input("Enter author ID: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")

author = Author.find_by_id(session, author_id)
if not author:
    print("Author not found. Please enter a valid author ID.")
    exit()

while True:
    name = input("Enter author name: ").strip()
    if not name:
        print("Input cannot be empty. Please try again.")
        exit()
    break

existing_author = session.query(Author).filter_by(name=name).first()
if existing_author:
    print("Duplicate entry. This author already exists.")
    exit()

print("Database seeded successfully!")
