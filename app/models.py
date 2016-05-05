from . import db
import random

class User(db.Model):   
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

class Wishlist(db.Model):
    __tablename__='wishlist'
    wishlist_id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    url=db.Column(db.String(100))
    description=db.Column(db.String(250))
    thumbnail=db.Column(db.String(100))
    user_id=db.Column(db.Integer,db.ForeignKey('user.user_id'))
    
    def __init__(self,title,url,description,thumbnail,user_id):
        self.title=title
        self.url=url
        self.description=description
        self.thumbnail=thumbnail
        self.user_id=user_id
        
    def is_authenticated(self):
        return True
        
    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id) 
            
            
class Token(db.Model):
    __tablename__ = 'tokens'
    userid = db.Column(db.Integer, db.ForeignKey('persons.id'))
    token = db.Column(db.String(255), primary_key=True)

    def __init__(self,userid):
        self.userid = userid
        tokens = db.session.query(Token).all()
        tokens = map(lambda x:x.token,tokens)
        token = tokenGenerator()
        while token in tokens:
            token = tokenGenerator()
        self.token = token

def tokenGenerator():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range (16))
