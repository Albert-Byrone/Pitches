from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProf(FlaskForm):
    bio = TextAreaField('Write something about you',validators=[Required()])
    submit = SubmitField('Update')

