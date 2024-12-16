import os

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')  # Used for session management, etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable Flask-SQLAlchemy modification tracking
    SQLALCHEMY_ECHO = False  # Set to True to log all SQL queries
    # Add more common settings here...

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI', 'postgresql://postgres:mysecretpassword@localhost/mydatabase')

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI', 'postgresql://postgres:mysecretpassword@localhost/mydatabase_test')
    WTF_CSRF_ENABLED = False  # Disables CSRF protection during testing

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:Noander!123@localhost/expensio')
    # Additional production-specific settings (e.g., logging, security, etc.)
    # For example:
    # LOGGING_LEVEL = 'ERROR'

# Select the appropriate configuration based on the environment variable
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

# You can access the selected config as follows:
# app.config.from_object(config[os.getenv('FLASK_ENV', 'development')])
