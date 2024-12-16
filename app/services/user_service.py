from app.models.user_model import User
from app import db  # Assuming you're using SQLAlchemy for ORM

def add_user(data):
    user = User(name=data['name'], age=data['age'])
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

def get_users():
    users = User.query.all()
    return [user.to_dict() for user in users]
