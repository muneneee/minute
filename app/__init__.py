from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options
from flask_sqlalchemy import SQLAlchemy
from flask-login import LoginManager
import os


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    #init app
    app = Flask(__name__)

    #setting configs
    app.config.from_object(Config_options[config_name])

    app.config.update(SECRET_KEY =os.urandom(24))



    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app