from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!!!!</p>"

@app.route("/")
def main():
  return render_template('main.html')

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