from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.Model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref='user',lazy='dynamic')
    comment = db.relationship('Comment',backref='user',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic') 

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()
