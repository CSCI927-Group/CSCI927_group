from flask import Blueprint, current_app, session, request, render_template, redirect, url_for, jsonify,flash
import json
from .objects import Order, Event, EventUpdate, Ticketing
from . import db
from .init import init_data

app = Blueprint('app', __name__,  static_url_path='/src',static_folder='src')
def log(event):
    id, name, email = getUser()
    current_app.logger.info(f'{id}, {name}, {event}, CUSTOMLOG')

def getUser():
    return [
        session.get('user_id', 0),
        session.get('user_name', 'anonymous'),
        session.get('user_email', 'none')
    ]
#
##
### Route logic

# @app.route('/init_data')
# def init_data_interface():
#     init_data()
#     return 'Init data success!'

@app.route("/")
def index():
    if request.args.get('user_id'):
        session['user_id'] = request.args.get('user_id')
        session['user_name'] = request.args.get('user_name')
        session['user_email'] = request.args.get('user_email')

    log("enter index")
    return render_template('index.html')

import os
from flask import send_from_directory

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

@app.route('/availability/<int:event_id>')
def availability(event_id):
    tickets = Ticketing.query.filter_by(event_id=event_id).all()  
    return render_template('availability.html', tickets=tickets)

# Payment page using GET (collects email)
@app.route('/payment', methods=['GET'])
def payment():
    ticket_id = request.args.get('ticket_id') 
    email = getUser()[2] # request.args.get('email') 
    quantity = request.args.get('quantity', 1) 

    if email and ticket_id:
        return redirect(url_for('app.payment_success', email=email, ticket_id=ticket_id, quantity=quantity))
    
    return render_template('payment.html', ticket_id=ticket_id)

@app.route('/payment-success')
def payment_success():
    email = request.args.get('email')  
    ticket_id = request.args.get('ticket_id')  
    quantity = int(request.args.get('quantity', 1))  

    if ticket_id and email and quantity > 0:
        success = book_ticket(ticket_id, email, quantity)
    #     if success:
    #         flash(f"Payment successful and {quantity} ticket(s) booked!", "success")
    #     else:
    #         flash("Payment successful but no tickets available for this time slot.", "danger")
    # else:
    #     flash("Missing email, ticket information, or invalid quantity.", "danger")

    return render_template('payment_success.html', email=email)

#my booking page
# @app.route('/my_booking')
# def my_booking():
#     log("enter my booking page")
#     return render_template('my_booking.html')
# @app.route('/my-booking-check', methods=['GET'])
# def my_booking_check():
#     email = request.args.get('email')
#     bookings = Ticketing.query.filter_by(email=email).all()  
#     if bookings:
#         return render_template('my_booking_tickets.html', bookings=bookings, email=email)
#     else:
#         # flash("Email not found. Please try again.", "danger")
#         return redirect(url_for('my_booking'))
# Booking Check Page
@app.route('/my-booking-check', methods=['GET'])
def my_booking_check():
    email = request.args.get('email')
    
    # If no email provided, render an error message directly in the template
    if not email:
        return render_template('my_booking_tickets.html', bookings=[], email=email, message="No email provided. Please try again.")

    # Query bookings based on email
    bookings = Ticketing.query.filter_by(email=email).all()

    if bookings:
        # If bookings exist, render the booking tickets page
        return render_template('my_booking_tickets.html', bookings=bookings, email=email, message=None)
    else:
        # No bookings found, display a message on the same page
        return render_template('my_booking_tickets.html', bookings=[], email=email, message="No bookings found for this email.")


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