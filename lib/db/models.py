
    
    
    
    
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