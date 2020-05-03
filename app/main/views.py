from flask import render_template
from app import app

@app.route('/')
def index():

    title = 'Welcome to pitcher'

    return render_template('index.html', title = title)