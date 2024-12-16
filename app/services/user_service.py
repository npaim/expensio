from app.db import db
from app.models.user_model import User

def add_user(name, age):
    """Adds a user to the database."""
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_users():
    """Fetches all users from the database."""
    return User.query.all()
