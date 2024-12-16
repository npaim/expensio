from flask import Flask
from app.db import db  # Import db from the new module
from app.routes.user_routes import user_routes

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(user_routes, url_prefix='/users')

    # Create tables
    with app.app_context():
        db.create_all()

    return app
