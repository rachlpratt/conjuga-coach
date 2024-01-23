import os

from flask import Flask

from .extensions import db
from .routes import main
import config


def create_app():
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))

    app = Flask(__name__, instance_relative_config=True,
                instance_path=os.path.join(base_dir, 'instance'))

    flask_env = os.environ.get('FLASK_ENV', 'development').lower()

    if flask_env == "production":
        app.config.from_object(config.ProductionConfig)
    elif flask_env == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    from . import models
    db.init_app(app)

    app.register_blueprint(main)
    return app
