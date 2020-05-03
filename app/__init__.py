from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options
from flask_sqlalchemy import SQLAlchemy
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


     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app