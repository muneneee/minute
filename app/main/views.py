from flask import render_template, request,redirect,url_for, abort
from . import main
from .forms import UpdateProfile,PitchForm
from flask_login import login_required
from .. import db,photos
from ..models import User,Pitch


@main.route('/')
def index():

    title = 'Welcome to pitcher'
    pitches = Pitch.get_pitches()

    return render_template('index.html', title = title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form = form)


@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))



@main.route('/pitch', methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        new_pitch = Pitch(title,pitch)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))


    title = 'New Pitch'
    return render_template('pitch.html' ,title = title, pitch_form = form) 

