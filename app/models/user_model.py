from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age}
