from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login  import login_user,login_required,logout_user
from .form import LoginForm,RegisterForm
from ..models import User
from flask_login import login_user
from ..email import mail_message
