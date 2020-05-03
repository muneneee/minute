from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig


#init app
app = Flask(__name__)

#setting configs


#init flask extensions
bootstrap = Bootstrap(app)

from .main import views