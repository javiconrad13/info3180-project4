from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys 

app = Flask(__name__)
#TO ADD app.config
db = SQLAlchemy(app)
db.create_all()

from app import views,models

