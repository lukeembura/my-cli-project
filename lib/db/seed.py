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

# Seed Books
Book.create(session, title="Things Fall Apart", author_id=author1.id)
Book.create(session, title="No Longer at Ease", author_id=author1.id)
Book.create(session, title="The River Between", author_id=author2.id)
Book.create(session, title="Weep Not, Child", author_id=author2.id)
Book.create(session, title="The River and the Source", author_id=author3.id)

print("Database seeded successfully!")
