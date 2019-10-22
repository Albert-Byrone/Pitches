from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password  = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    password_confirm =PasswordField('Confrim Password',validators=[Required()])
    submit = SubmitField('Sign Up')

