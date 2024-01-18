from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import main
from backend import config
import os

db = SQLAlchemy()


def create_app():
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))

    app = Flask(__name__, instance_relative_config=True,
                instance_path=os.path.join(base_dir, 'instance'))

    from . import models

    flask_env = os.environ.get('FLASK_ENV', 'development').lower()

    if flask_env == "production":
        app.config.from_object(config.ProductionConfig)
    elif flask_env == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)

    app.register_blueprint(main)
    return app
