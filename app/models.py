from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))


    pitches = db.relationship('Pitch',backref = 'user' , lazy = "dynamic")
    liked =db.relationship('PitchLike', foreign_keys = 'PitchLike.user_id', backref='user', lazy = 'dynamic')


    def like_pitch(self, pitch):
        if not self.has_liked_pitch(pitch):
            like = PitchLike(user_id=self.id,pitch_id = pitch.id)
            db.session.add(like)

    
    def unlike_pitch(self, pitch):
        if self.has_liked_pitch(pitch):
            PitchLike.query.filter_by(user_id=self.id, pitch_id = pitch.id).delete()

    
    def has_liked_pitch(self, pitch):
        return PitchLike.query.filter(PitchLike.user_id == self.id, PitchLike.pitch_id ==pitch.id).count() > 0


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name}'



class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    category = db.Column(db.String)
    pitch_title = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    author = db.Column(db.Integer,db.ForeignKey("users.id"))

    
    likes = db.relationship('PitchLike', backref = 'pitch', lazy ='dynamic')


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.filter_by().all()
        return pitches

    @classmethod
    def get_all_pitches(cls):
        pitches = Pitch.query.order_by('-id').all()
        return pitches


    def __repr__(self):
        return f'Pitch {self.pitch_title}'



class PitchLike(db.Model):
    __tablename__= 'pitch_like'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
