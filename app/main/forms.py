from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required




class PitchForm(FlaskForm):


    category = SelectField('Category', choices=[('Pickup-Lines','Pickup Lines'), ('Interview-Pitch', 'Inerview Pitch'), ('Famous-Quotes', 'Famous Quotes'), ('Bible-Verses', 'Bible Verses')] ,validators=[Required()])
    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators =[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField("Leave a comment", validators = [Required()])
    submit = SubmitField("Post")