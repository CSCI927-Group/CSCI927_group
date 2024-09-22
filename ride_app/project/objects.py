from . import db
from enum import Enum

class OrderEnum(Enum):
    INIT = 1
    PAID = 2
    ONBOARD = 3
    COMPLETE = 4
    CANCEL = 5
    INVAILD = 6

class Order(db.Model):
    # use to json serialization 
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    state = db.Column(db.Integer)
    datetime = db.Column(db.Integer)
    
class OrderBill(db.Model):
    # use to json serialization 
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    order_id = db.Column(db.Integer)
    datetime = db.Column(db.Integer)
    has_pay = db.Column(db.Boolean)