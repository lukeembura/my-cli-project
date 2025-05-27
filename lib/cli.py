from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Author, Book

DATABASE_URL = "sqlite:///lib/db/library.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()