from . import db
import random

 __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)  
    first_name = db.Column(db.String(80))     
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)    
    password = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)
    tokens = db.relationship('Token',backref='user')

def __init__(self,first_name,last_name,username,password,email,addon):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.password = password
    self.email = email

def is_authenticated(self):
    return True

def is_active(self):
    return True

def is_anonymous(self):
    return False

def get_id(self):
    try:
        return unicode(self.user_id)
        except NameError:
            return str(self.user_id)  
            
def __repr__(self):
    return '<User %r>' % (self.username)           
