
    
    @classmethod
    def create(cls, session, name):
        author = cls(name=name)
        session.add(author)
        session.commit()
        return author

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    def delete(self, session):
        session.delete(self)
        session.commit()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author_id={self.author_id})>"

    @validates('title')
    def validate_title(self, key, value):
        if not value or len(value.strip()) == 0:
            raise ValueError("Book title cannot be empty.")
        return value

    @classmethod
    def create(cls, session, title, author):
        book = cls(title=title, author=author)
        session.add(book)
        session.commit()
        return book

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    def delete(self, session):
        session.delete(self)
        session.commit()