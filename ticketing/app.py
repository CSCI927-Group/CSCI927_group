from flask import Flask, render_template, redirect, url_for, request,flash

app = Flask(__name__)
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Event data (for simulation)
events = {
    1: {
        'title': 'Concert at Central Park',
        'date': 'September 25, 2024',
        'description': 'Enjoy a live concert in the heart of Central Park featuring popular bands and artists.',
        'image': 'https://via.placeholder.com/800x400'
    },
    2: {
        'title': 'Food Festival',
        'date': 'October 1, 2024',
        'description': 'A celebration of culinary arts with food trucks, chefs, and a variety of delicious foods.',
        'image': 'https://via.placeholder.com/800x400'
    },
    3: {
        'title': 'Art Exhibition',
        'date': 'October 10, 2024',
        'description': "Discover modern and contemporary art at the city's largest art exhibition.",
        'image': 'https://via.placeholder.com/800x400'
    }
}
# Mock booking data
bookings = {
    "stanleyhuang0824@gmail.com": [
        {"event": "Concert at Central Park", "date": "September 25, 2024", "tickets": 2},
        {"event": "Art Exhibition", "date": "October 10, 2024", "tickets": 1}
    ],
    "heyinwong992@gmail.com": [
        {"event": "Food Festival", "date": "October 1, 2024", "tickets": 4}
    ]
}


# Route for ticket availability page
@app.route('/availability')
def availability():
    tickets = [
        {'date': 'September 20, 2024', 'available': True},
        {'date': 'September 21, 2024', 'available': False},
        {'date': 'September 22, 2024', 'available': True}
    ]
    return render_template('availability.html', tickets=tickets)

# Payment page using GET (collects email)
@app.route('/payment', methods=['GET'])
def payment():
    email = request.args.get('email')  # Get the email from the query string
    if email:
        # Redirect to the payment success page with the email
        return redirect(url_for('payment_success', email=email))
    
    # Render the payment form if email is not provided
    return render_template('payment.html')

# Payment success page with email confirmation
@app.route('/payment-success')
def payment_success():
    email = request.args.get('email')  # Get the email from the query string
    return render_template('payment_success.html', email=email)

#my booking page
@app.route('/my_booking')
def my_booking():
    return render_template('my_booking.html')

# @app.route('/my-booking-check', methods=['GET'])
# def my_booking_check():
#     email = request.args.get('email')
#     if email in bookings:
#         return render_template('my_booking_tickets.html', bookings=bookings[email], email=email)
#     else:
#         return "No bookings found for this email."
    
@app.route('/my-booking-check', methods=['GET'])
def my_booking_check():
    email = request.args.get('email')
    if email in bookings:
        return render_template('my_booking_tickets.html', bookings=bookings[email], email=email)
    else:
        flash("Email not found. Please try again.", "danger")
        return redirect(url_for('my_booking'))


#Browse event page
@app.route('/browse_events')
def browse_events():
    return render_template('browse_events.html')

# Route for the "News" page
@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/event-info/<int:event_id>')
def event_info(event_id):
    event = events.get(event_id)
    if event:
        return render_template('event_info.html', event=event)
    else:
        return "Event not found", 404

if __name__ == '__main__':
    app.run(debug=True)