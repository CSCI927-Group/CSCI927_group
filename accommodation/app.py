from flask import Flask, render_template, redirect, url_for, request, flash, session
from data import accommodation_data, news_data, updates_data, bookings, events

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Home page route
@app.route('/')
def layout_content():
    return render_template('layout_content.html')

# Route for ticket availability page
@app.route('/availability')
def availability():
    return render_template('availability.html', accommodations=accommodation_data)

# Payment page using GET (collects email)
@app.route('/payment', methods=['GET'])
def payment():
    email = request.args.get('email')  # Collect email via GET
    if email:
        return redirect(url_for('payment_success', email=email))
    return render_template('payment.html')

@app.route('/payment-success')
def payment_success():
    email = request.args.get('email')  # Get the email from the query parameters
    return render_template('payment_success.html', email=email)

# My booking page
@app.route('/my_booking')
def my_booking():
    return render_template('my_booking.html')

@app.route('/my-booking-check', methods=['GET'])
def my_booking_check():
    email = request.args.get('email')
    if email in bookings:
        return render_template('my_booking_acc.html', bookings=bookings[email], email=email)
    else:
        flash("Email not found. Please try again.", "danger")
        return redirect(url_for('my_booking'))

# Browse events page
@app.route('/browse_accommodations')
def browse_accommodations():
    return render_template('browse_accommodations.html', events=events)

@app.route('/event-info/<int:event_id>')
def event_info(event_id):
    event = events.get(event_id)
    if event:
        return render_template('event_info.html', event=event)
    else:
        return "Event not found", 404

# News and updates
@app.route('/simple_reviews')
def simple_reviews():
    return render_template('simple_reviews.html', news_data=news_data, updates_data=updates_data)

@app.route('/simple_reviews/<int:news_id>')
def news_detail(news_id):
    news_item = news_data.get(news_id)
    if news_item:
        return render_template('news_detail.html', item=news_item)
    else:
        return "News item not found", 404

@app.route('/update/<int:update_id>')
def update_detail(update_id):
    update_item = updates_data.get(update_id)
    if update_item:
        return render_template('update_detail.html', item=update_item)
    else:
        return "Update item not found", 404

# User login
@app.route('/login_account', methods=['GET'])
def login_account():
    email = request.args.get('email')
    password = request.args.get('password')  # Get user password

    if email:
        session['user_email'] = email  # Store user email in session
        flash("Login successful!")  # Flash a success message
        return redirect(url_for('browse_accommodations'))
    
    return render_template('login_account.html')

@app.route('/cancel_booking', methods=['GET'])
def cancel_booking():
    booking_id = request.args.get('bookingId')
    email = request.args.get('email')
    
    # success!
    if booking_id and email:
        flash('Booking cancelled successfully.', 'success')
        return redirect(url_for('my_booking'))
    
    return render_template('cancel_booking.html')



@app.route('/review_content', methods=['GET'])
def review_content():
    return render_template('review_content.html')








if __name__ == '__main__':
    app.run(debug=True)
