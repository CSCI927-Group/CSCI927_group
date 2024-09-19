from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Simulate ticket availability in a dictionary (you should replace this with a database)
ticket_availability = {
    '2024-09-20': True,
    '2024-09-21': False,
    '2024-09-22': True
}

# Route to check availability
@app.route('/check_availability', methods=['GET'])
def check_availability():
    date = request.args.get('date')
    available = ticket_availability.get(date, False)
    return jsonify({'available': available})

# Route to book tickets
@app.route('/book_tickets', methods=['POST'])
def book_tickets():
    num_tickets = request.form.get('num_tickets')
    # Handle booking logic here (e.g., save to database)
    return jsonify({'success': True, 'message': f'{num_tickets} tickets booked successfully!'})


@app.route("/")
def main():
  return render_template('main.html',tickets=tickets)

@app.route("/ticket.html")
def ticket():
  return render_template('ticket.html')

@app.route("/ride")
def ride():
  return render_template('ride.html')

@app.route('/ride/route', methods=['GET'])
def ride_route():
  context = {
    'location': request.args.get('location', ''),
    'destination': request.args.get('destination', ''),
    'routes': [
      { 'id': 1, 'name': 'Route A', 'price': 10 },
      { 'id': 2, 'name': 'Route B', 'price': 20 },
      { 'id': 3, 'name': 'Route C', 'price': 30 },
    ]
  }
  return render_template('ride_route.html', **context)

@app.route('/ride/payment', methods=['GET'])
def ride_payment():
  context = {
    'location': request.args.get('location', ''),
    'destination': request.args.get('destination', ''),
    'routes': [
      { 'id': 1, 'name': 'Route A', 'price': 10 },
      { 'id': 2, 'name': 'Route B', 'price': 20 },
      { 'id': 3, 'name': 'Route C', 'price': 30 },
    ]
  }
  return render_template('ride_payment.html', **context)