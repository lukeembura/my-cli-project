from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nationality = Column(String)

    # Relationship to books
    books = relationship('Book', back_populates='author', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}', nationality='{self.nationality}')>"

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)  # Primary key is required!
    title = Column(String, nullable=False)
    genre = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    # Relationship to author
    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', genre='{self.genre}', author_id={self.author_id})>"
