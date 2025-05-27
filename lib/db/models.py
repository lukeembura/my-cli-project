from sqlalchemy.orm import Session, relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="author", cascade="all, delete")

    # ORM methods
    @classmethod
    def create(cls, session: Session, name: str):
        author = cls(name=name)
        session.add(author)
        session.commit()
        return author

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session: Session, author_id: int):
        return session.query(cls).filter_by(id=author_id).first()

    def delete(self, session: Session):
        session.delete(self)
        session.commit()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship("Author", back_populates="books")

    # ORM methods
    @classmethod
    def create(cls, session: Session, title: str, author_id: int):
        book = cls(title=title, author_id=author_id)
        session.add(book)
        session.commit()
        return book

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session: Session, book_id: int):
        return session.query(cls).filter_by(id=book_id).first()

    def delete(self, session: Session):
        session.delete(self)
        session.commit()
