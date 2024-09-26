from flask import Flask, render_template, redirect, url_for, request,flash
from flask_sqlalchemy import SQLAlchemy

# from data import ticket_data,news_data,updates_data,bookings,events

app = Flask(__name__, static_folder='src')
app.secret_key = 'your_secret_key'  # Needed for flashing messages


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200))
    additional_info = db.Column(db.Text, nullable=True)


    ticketings = db.relationship('Ticketing', backref='event', lazy=True)
    updates = db.relationship('EventUpdate', backref='event', lazy=True)

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

def book_ticket(ticket_id, email, quantity):
    ticket = Ticketing.query.get(ticket_id)
    if ticket and ticket.available_tickets >= quantity:
        ticket.email = email  
        ticket.available_tickets -= quantity  
        ticket.booked_quantity = quantity  
        db.session.commit()
        return True
    else:
        return False
    
# Home page route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/availability/<int:event_id>')
def availability(event_id):
    tickets = Ticketing.query.filter_by(event_id=event_id).all()  
    return render_template('availability.html', tickets=tickets)

# Payment page using GET (collects email)
@app.route('/payment', methods=['GET'])
def payment():
    ticket_id = request.args.get('ticket_id') 
    email = request.args.get('email') 

    if email and ticket_id:
        return redirect(url_for('payment_success', email=email, ticket_id=ticket_id))
    
    return render_template('payment.html', ticket_id=ticket_id)

@app.route('/payment-success')
def payment_success():
    email = request.args.get('email')  
    ticket_id = request.args.get('ticket_id')  
    quantity = int(request.args.get('quantity', 1))  

    if ticket_id and email and quantity > 0:
        success = book_ticket(ticket_id, email, quantity)
        if success:
            flash(f"Payment successful and {quantity} ticket(s) booked!", "success")
        else:
            flash("Payment successful but no tickets available for this time slot.", "danger")
    else:
        flash("Missing email, ticket information, or invalid quantity.", "danger")

    return render_template('payment_success.html', email=email)

#my booking page
@app.route('/my_booking')
def my_booking():
    return render_template('my_booking.html')
@app.route('/my-booking-check', methods=['GET'])
def my_booking_check():
    email = request.args.get('email')
    bookings = Ticketing.query.filter_by(email=email).all()  
    if bookings:
        return render_template('my_booking_tickets.html', bookings=bookings, email=email)
    else:
        flash("Email not found. Please try again.", "danger")
        return redirect(url_for('my_booking'))


#Browse event page
@app.route('/browse_events')
def browse_events():
    events = Event.query.all()  
    return render_template('browse_events.html', events=events)

@app.route('/event-info/<int:event_id>')
def event_info(event_id):
    event = Event.query.get(event_id)  
    if event:
        return render_template('event_info.html', event=event)  
    else:
        return "Event not found", 404
    
@app.route('/news')
def news():
    news_data = EventUpdate.query.filter_by(type='news').all()  
    updates_data = EventUpdate.query.filter_by(type='update').all()  
    return render_template('news.html', news_data=news_data, updates_data=updates_data)

@app.route('/news/<int:news_id>')
def news_detail(news_id):
    item = EventUpdate.query.get_or_404(news_id)  
    return render_template('news_detail.html', item=item)

@app.route('/update/<int:update_id>')
def update_detail(update_id):
    item = EventUpdate.query.get_or_404(update_id)  
    return render_template('update_detail.html', item=item)
    
if __name__ == '__main__':
    app.run(debug=True)
