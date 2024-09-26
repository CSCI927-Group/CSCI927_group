from flask import Blueprint, current_app, session, request, render_template, redirect, url_for, jsonify
import json
from .objects import Order, OrderEnum, Hotel, Review
from . import db
from .init import init_data

app = Blueprint('app', __name__)
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
    session['user_id'] = request.args.get('user_id')
    session['user_name'] = request.args.get('user_name')
    session['user_email'] = request.args.get('user_email')
    return render_template('welcome.html')

### Hotel
@app.route("/hotels")
def hotel_index():
    log('enter test page')
    hotel_list = Hotel.query.all()
    # id = getUser()[0]
    # order = Hotel.query.filter_by(id=id)
    return render_template("hotel-index.html", list=hotel_list)

@app.route("/order/add", methods=['POST'])
def order_add():
    uid = getUser()[0]
    id = request.form.get('id')
    price = request.form.get('price')
    startDate = request.form.get('startDate')
    endDate = request.form.get('endDate')
    status = OrderEnum.ORDER.value
    
    hotel = Hotel.query.filter_by(id=id).first()
    order = Order(name=hotel.name, price=price, startDate=startDate, endDate=endDate, status=status, uid=uid)
    db.session.add(order)
    db.session.commit()
    return 'Add order success!'

@app.route("/order/cancel", methods=['Delete'])
def order_cancel():    

    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        return 'Delete order success!' 
    else:
        return 'No found order'

@app.route("/order/checkin", methods=['PUT'])
def order_checkin():
    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()
    order.status = OrderEnum.CHECK_IN.value
    db.session.commit()
    return 'Update order success!'

@app.route("/order/checkout", methods=['PUT'])
def order_checkout():
    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()
    order.status = OrderEnum.CHECK_OUT.value
    db.session.commit()
    return 'Update order success!'

@app.route("/reviews")
def review_list():
    log('enter review page')
    review_list = Review.query.all()
    return render_template("test.html", list=review_list)

@app.route("/reviews/add", methods=['POST'])
def review_add():
    uid = getUser()[0]
    oid = request.form.get('id')
    description = request.form.get('description')

    review = Review(uid=uid, oid=oid, description=description)
    db.session.add(review)
    db.session.commit()
    return 'Add review success!'


@app.route("/hotel-order")
def hotel_order():
    return render_template("hotel-order.html")

@app.route("/hotel_payment_info")
def hotel_payment_info():
    return render_template("hotel_payment_info.html")

@app.route("/hotel_payment_success")
def hotel_payment_success():
    return render_template("hotel_payment_success.html")


@app.route("/order-list")
def order_list():
    # list = Order.query.filter_by(user_id=id)
    list = Order.query.all()
    order_state = { state.value: state.name.lower() for state in OrderEnum}
    return render_template("order-list.html", list=list, order_state=order_state)

@app.route('/review_content', methods=['GET'])
def review_content():
    return render_template('review_content.html')

