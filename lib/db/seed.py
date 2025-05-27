from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Author, Book

# Create a database engine
engine = create_engine('sqlite:///lib/db/library.db')
Session = sessionmaker(bind=engine)
session = Session()


# Optional: Clear old data (for clean re-seeding)
session.query(Book).delete()
session.query(Author).delete()


# Create authors
author1 = Author(name="Ngũgĩ wa Thiong'o", country="Kenya")
author2 = Author(name="Chinua Achebe", country="Nigeria")
author3 = Author(name="Margaret Ogola", country="Kenya")

# Create books
book1 = Book(title="Petals of Blood", genre="Fiction", author=author1)
book2 = Book(title="Weep Not, Child", genre="Fiction", author=author1)
book3 = Book(title="Things Fall Apart", genre="Historical", author=author2)
book4 = Book(title="The River and the Source", genre="Drama", author=author3)
