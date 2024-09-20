from flask import Blueprint, current_app, session, request, render_template, redirect, url_for, jsonify
import json
from .objects import Order
from . import db

app = Blueprint('app', __name__)
def log(event):
    user_id = session.get('user_id')
    user_name = session.get('user_name')
    current_app.logger.info(f'{user_id}, {user_name}, {event}, CUSTOMLOG')

#
##
### Route logic
@app.route("/")
def index():
    session['user_id'] = request.args.get('user_id', 'default_id')
    session['user_name'] = request.args.get('user_name', 'default_name')
    return redirect(url_for('app.ride')) # <--- rename to module's index name


@app.route("/ride")
def ride():
    log('enter ride page')
    return render_template("ride.html")


@app.route("/ride/route", methods=["GET"])
def ride_route():
    context = {
        "location": request.args.get("location", ""),
        "destination": request.args.get("destination", ""),
        "routes": [
            {"id": 1, "name": "Route A", "price": 10},
            {"id": 2, "name": "Route B", "price": 20},
            {"id": 3, "name": "Route C", "price": 30},
        ],
    }
    return render_template("ride_route.html", **context)


@app.route("/ride/payment", methods=["GET"])
def ride_payment():
    context = {
        "location": request.args.get("location", ""),
        "destination": request.args.get("destination", ""),
        "routes": [
            {"id": 1, "name": "Route A", "price": 10},
            {"id": 2, "name": "Route B", "price": 20},
            {"id": 3, "name": "Route C", "price": 30},
        ],
    }
    return render_template("ride_payment.html", **context)
