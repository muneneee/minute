from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    #init app
    app = Flask(__name__)

    #setting configs
    app.config.from_object(Config_options[config_name])
    Config_options[config_name].init_app(app)

    app.config.update(SECRET_KEY =os.urandom(24))


     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app