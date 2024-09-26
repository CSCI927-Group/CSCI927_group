from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    index = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(1000)) # module page url
    photo = db.Column(db.String(1000)) # describe image
    time = db.Column(db.Integer)    # update time
    online = db.Column(db.Boolean) # describe state
    authorization = db.Column(db.Boolean) # describe whether need to login