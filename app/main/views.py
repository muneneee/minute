from flask import render_template
from . import main


@main.route('/')
def index():

    title = 'Welcome to pitcher'

    return render_template('index.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)