from flask import Blueprint, current_app, session, request, render_template, redirect, url_for, jsonify
from datetime import datetime
from .objects import Order, OrderEnum, Hotel, Review
from . import db
from .init import init_data

app = Blueprint('app', __name__, static_folder='assets')

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
    log('Enter welcome page')
    return render_template('welcome.html')

### Hotel
@app.route("/hotels")
def hotel_index():
    hotel_list = Hotel.query.all()
    log('Enter hotel index page')
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
    log(f'Add hotel {id} order')
    return { 'order_id': order.id } # 'Add order success!'

@app.route("/order/checkin", methods=['PUT'])
def order_checkin():
    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()
    order.status = OrderEnum.CHECK_IN.value
    db.session.commit()
    log('Hotel check-in')
    return 'Checkin success!'

@app.route("/order/checkout", methods=['PUT'])
def order_checkout():
    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()
    order.status = OrderEnum.CHECK_OUT.value
    db.session.commit()
    log('Hotel check-out')
    return 'Checkout success!'

@app.route("/reviews")
def review_list():
    log('enter review page')
    review_list = Review.query.all()
    return render_template("review-list.html", list=review_list)

@app.route("/reviews/update", methods=['POST'])
def review_update():
    oid = request.form.get('oid')
    rating = request.form.get('rating')
    review = request.form.get('review')
    
    order = Order.query.filter_by(id=oid).first()
    if not order:
        return jsonify({'error': 'Order not found'}), 404  # Return JSON error if order is not found
    order.status = OrderEnum.REVIEWED.value    

    record = Review.query.filter_by(oid=oid).first()

    date = datetime.now().strftime('%Y-%m-%d')
    if not record:
        record = Review(oid=oid, date=date, rating=rating, review=review)
        db.session.add(record)
        db.session.commit()
        return 'Add review success!'
    else:
        record.date = date
        record.rating = rating
        record.review = review
        db.session.commit()
        return 'Update review success!'

@app.route("/hotel-order")
def hotel_order():
    return render_template("hotel-order.html")

@app.route("/hotel_payment_info")
def hotel_payment_info():
    return render_template("hotel_payment_info.html")

@app.route("/hotel_payment_success")
def hotel_payment_success():
    return render_template("hotel_payment_success.html")

@app.route("/hotel_check_in")
def hotel_check_in():
    return render_template('hotel_check_in.html')

@app.route("/hotel_check_out")
def hotel_check_out():
    return render_template('hotel_check_out.html')

@app.route("/order-list")
def order_list():
    list = Order.query.all()
    order_state = { state.value: state.name.lower() for state in OrderEnum }
    return render_template("order-list.html", list=list, order_state=order_state)

@app.route('/review_submit', methods=['GET'])
def review_submit():
    oid = request.args.get('id')
    record = Review.query.filter_by(oid=oid).first()
    log('Submit review')
    return render_template('review_submit.html', record=record)

@app.route('/order/delete', methods=['DELETE'])  # New route to delete an order
def delete_order():
    order_id = request.args.get('id', type=int)
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        log('Delete hotel order')
        return jsonify({'message': 'Order deleted successfully.'}), 200
    return jsonify({'message': 'Order not found.'}), 404

@app.route('/cancel_order', methods=['PUT'])
def cancel_order():
    order_id = request.args.get('id')
    order = Order.query.get(order_id)
    
    if order:
        order.status = OrderEnum.CANCEL.value  # Update status to cancelled
        db.session.commit()
        log('Cancel hotel order')
        return jsonify({'message': 'Order has been cancelled'}), 200
    return jsonify({'message': 'Order not found'}), 404


@app.route("/order/pay", methods=['PUT'])
def order_pay():
    try:
        id = request.args.get('id')
        
        if not id:
            return jsonify({'error': 'Order ID is required'}), 400  # Return JSON error if ID is not provided

        order = Order.query.filter_by(id=id).first()
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404  # Return JSON error if order is not found

        order.status = OrderEnum.ORDER.value
        db.session.commit()
        log('Complete hotel order payment')
        
        # Prepare response data
        response_data = {
            'message': 'Complete payment!',
            'order_id': order.id,
            'new_status': order.status
        }
        
        return jsonify(response_data), 200  # Return JSON response for successful update
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500  # Return JSON error and output exception message