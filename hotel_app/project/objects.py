from . import db
from enum import Enum

class OrderEnum(Enum):
    UNPAY = 0
    ORDER = 1
    CHECK_IN = 2
    CHECK_OUT = 3
    REVIEWED = 4
    CANCEL = 5

class Hotel(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    image = db.Column(db.String(1000))
    price = db.Column(db.Integer)

class Order(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    name = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    startDate = db.Column(db.Integer)
    endDate = db.Column(db.Integer)
    status = db.Column(db.Integer)

    @staticmethod
    def delete_order(order_id):
        order = Order.query.get(order_id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return True
        return False

class Review(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    oid = db.Column(db.Integer)
    description = db.Column(db.String(1000))
