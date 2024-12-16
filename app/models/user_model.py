from app.db import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'expensio'}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
