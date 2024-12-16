from flask import Flask
from app.routes.user_routes import user_routes

def create_app():
    app = Flask(__name__)

    # Register Blueprints (modular routes)
    app.register_blueprint(user_routes, url_prefix='/users')

    return app