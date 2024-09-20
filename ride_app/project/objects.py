from . import db

class Order(db.Model):
    # use to json serialization 
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    