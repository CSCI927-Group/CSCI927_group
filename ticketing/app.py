from flask import Flask, render_template, redirect, url_for, request,flash
from data import ticket_data,news_data,updates_data,bookings,events

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Home page route
@app.route('/')
def index():
    return render_template('index.html')


# Route for ticket availability page
@app.route('/availability')
def availability():
    return render_template('availability.html', tickets=ticket_data)

# Payment page using GET (collects email)
@app.route('/payment', methods=['GET'])
def payment():
    email = request.args.get('email')  # Collect email via GET
    if email:
        # Redirect to the payment success page with the email
        return redirect(url_for('payment_success', email=email))
    
    # Render the payment form if email is not provided
    return render_template('payment.html')

@app.route('/payment-success')
def payment_success():
    email = request.args.get('email')  # Get the email from the query parameters
    return render_template('payment_success.html', email=email)

#my booking page
@app.route('/my_booking')
def my_booking():
    return render_template('my_booking.html')
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
    return render_template('browse_events.html',events=events)

@app.route('/event-info/<int:event_id>')
def event_info(event_id):
    event = events.get(event_id)
    if event:
        return render_template('event_info.html', event=event)
    else:
        return "Event not found", 404
    
#MNews and updates
@app.route('/news')
def news():
    return render_template('news.html',news_data=news_data,updates_data=updates_data)

@app.route('/news/<int:news_id>')
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
    
if __name__ == '__main__':
    app.run(debug=True)
