from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    # app.config.from_object(DevConfig)
    # app.config.from_pyfile('config.py')

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    # bootstrap = Bootstrap(app)

    # Will add the views and forms
    # from main import views
    # from app import errors

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app


