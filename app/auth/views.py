from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login  import login_user,login_required,logout_user
from .form import LoginForm,RegisterForm
from ..models import User
from flask_login import login_user
from ..email import mail_message
from .. import db

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(username =form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username and password')
    return render_template('auth/login.html',loginform=form)

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username = form.username.data,password=form.password.data)
        user.save_user()
        mail_message("Welcome to Pitch-World","email/welcome_user", user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',reg_form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))