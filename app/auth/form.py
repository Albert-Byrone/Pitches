from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password  = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


