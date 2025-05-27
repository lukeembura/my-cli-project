
    
    
    
    
    
    def delete(self, session):
        session.delete(self)
        session.commit()