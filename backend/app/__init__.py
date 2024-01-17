from flask import Flask
from .routes import main
import config
import os


def create_app():
    app = Flask(__name__)

    flask_env = os.environ.get('FLASK_ENV', 'development').lower()

    if flask_env == "production":
        app.config.from_object(config.ProductionConfig)
    elif flask_env == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    app.register_blueprint(main)
    return app
