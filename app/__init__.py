from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class TestingConfig(Config):
    # In-memory database for faster tests
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        from app.models import models
        db.create_all()

    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
