from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required




class ReviewForm(FlaskForm):


    title = StringField('Pitch title',validators=[Required()])
    Pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators =[Required()])
    submit = SubmitField('Submit')
