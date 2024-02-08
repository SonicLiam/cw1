"""
This module contains the application factory and configuration.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Config:
    """
    Base configuration
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class TestingConfig(Config):
    """
    Configuration for testing
    """
    # In-memory database for faster tests
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        from app.models import models # Inlining the import to avoid circular import
        db.create_all()
        if app.config['TESTING'] is False and db.session.query(models.DistanceTravelledToWork).count() == 0:
            from app.import_data import import_all_data
            import_all_data()

    from app.routes import api_bp # Inlining the import to avoid circular import
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
