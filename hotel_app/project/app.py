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
    return render_template("hotel-index.html", list=hotel_list)

@app.route("/order/add", methods=['POST'])
def order_add():
    uid = getUser()[0]
    id = request.form.get('id')
    price = request.form.get('price')
    startDate = request.form.get('startDate')
    endDate = request.form.get('endDate')
    status = OrderEnum.UNPAY.value
    
    hotel = Hotel.query.filter_by(id=id).first()
    order = Order(name=hotel.name, price=price, startDate=startDate, endDate=endDate, status=status, uid=uid)
    db.session.add(order)
    db.session.commit()
    return 'Add order success!'

@app.route("/order/cancel", methods=['DELETE'])  # Change to DELETE
def order_cancel():    
    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        return 'Delete order success!' 
    else:
        return 'No order found'

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
    list = Order.query.all()
    order_state = { state.value: state.name.lower() for state in OrderEnum }
    return render_template("order-list.html", list=list, order_state=order_state)

@app.route('/review_submit', methods=['GET'])
def review_submit():
    return render_template('review_submit.html')

@app.route('/order/delete', methods=['DELETE'])  # New route to delete an order
def delete_order():
    order_id = request.args.get('id', type=int)
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully.'}), 200
    return jsonify({'message': 'Order not found.'}), 404

@app.route('/cancel_order', methods=['PUT'])
def cancel_order():
    order_id = request.args.get('id')
    order = Order.query.get(order_id)
    
    if order:
        order.status = OrderEnum.CANCEL.value  # Update status to cancelled
        db.session.commit()
        return jsonify({'message': 'Order has been cancelled'}), 200
    return jsonify({'message': 'Order not found'}), 404


@app.route("/order/pay", methods=['PUT'])
def order_pay():
    try:
        id = request.args.get('id')
        
        if not id:
            return 'Order ID is required', 400  # Return 400 error if ID is not provided

        order = Order.query.filter_by(id=id).first()
        
        if not order:
            return 'Order not found', 404  # Return 404 error if order is not found

        order.status = OrderEnum.ORDER.value
        db.session.commit()
        
        return 'Update order success!', 200  # Return 200 status code for successful update
    except Exception as e:
        return f'An error occurred: {str(e)}', 500  # Return 500 error and output exception message


@app.route("/order/start_review", methods=['PUT'])
def order_startReview():
    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()

    if not order:
        return jsonify({"error": "Order not found."}), 404

    # Update order status to 'Reviewed'
    order.status = OrderEnum.REVIEWED.value
    db.session.commit()

    return jsonify({"message": "Update order to reviewed success!"}), 200  # Return a JSON response



