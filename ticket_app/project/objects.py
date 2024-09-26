from . import db

class Order(db.Model):
    # use to json serialization 
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200))
    additional_info = db.Column(db.Text, nullable=True)


    # ticketings = db.relationship('Ticketing', backref='event', lazy=True)
    # updates = db.relationship('EventUpdate', backref='event', lazy=True)

class Ticketing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time_slot = db.Column(db.String(20), nullable=False)
    available_tickets = db.Column(db.Integer, nullable=False)
    booked_quantity = db.Column(db.Integer, nullable=True, default=0)
    email = db.Column(db.String(100), nullable=True)  


class EventUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(100))
    image = db.Column(db.String(200))
    read_time = db.Column(db.String(20))
    type = db.Column(db.String(20), nullable=False)  
