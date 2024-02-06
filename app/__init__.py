from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.routes import api_bp

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    # 配置 SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # 这里可以添加更多的配置，如注册蓝图等

    with app.app_context():
        from app.models import models
        db.create_all()

    app.register_blueprint(api_bp, url_prefix='/api')

    return app
