from flask import Blueprint, current_app, session, request, render_template, redirect, url_for, jsonify
import json
from .objects import Order, OrderEnum
from . import db

app = Blueprint('app', __name__)
def log(event):
    id, name = getUser()
    current_app.logger.info(f'{id}, {name}, {event}, CUSTOMLOG')

def getUser():
    return [
        session.get('user_id', 0),
        session.get('user_name', 'anonymous')
    ]
#
##
### Route logic
@app.route("/")
def index():
    session['user_id'] = request.args.get('user_id', 'default_id')
    session['user_name'] = request.args.get('user_name', 'default_name')
    return redirect(url_for('app.test')) # <--- rename to module's index name

### Hotel
@app.route("/hotels")
def hotel_list():
    log('enter test page')
    hotel_list = Hotel.query.all()
    return render_template("test.html", list=hotel_list)

@app.route("/order/add", methods=['POST'])
def order_add():
    uid = getUser()[0]
    name = request.form.get('name')
    price = request.form.get('price')
    startDate = request.form.get('startDate')
    endDate = request.form.get('endDate')
    status = OrderEnum.ORDER.value
    
    order = Order(name=name, price=price, startDate=startDate, endDate=endDate, status=status, uid=uid)
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

@app.route("/order/update", methods=['PUT'])
def order_update():
    id = request.form.get('id')
    order = Order.query.filter_by(id=id).first()
    order.status = request.form.get('status')
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
    price = request.form.get('description')

    review = Review(uid=uid, oid=oid, price=price)
    db.session.add(review)
    db.session.commit()
    return 'Add review success!'

@app.route("/test")
def test():
    log('enter test page')
    order_list = Order.query.all()
    return render_template("test.html", list=order_list)

@app.route("/test/add", methods=['POST'])
def test_add():
    name = request.form.get('name')
    price = request.form.get('price')
    order = Order(name=name, price=price)
    db.session.add(order)
    db.session.commit()
    return 'Add order success!'

@app.route("/test/delete", methods=['Delete'])
def test_delete():
    id = request.args.get('id')
    order = Order.query.filter_by(id=id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        return 'Delete order success!' 
    else:
        return 'No found order'

@app.route("/test/update", methods=['PUT'])
def test_update():
    id = request.form.get('id')
    order = Order.query.filter_by(id=id).first()
    order.name = request.form.get('name')
    order.price = request.form.get('price')
    db.session.commit()
    return 'Update order success!'

@app.route("/test/list", methods=['GET'])
def test_list():
    order_list = Order.query.all()
    order_dict = [result.as_dict() for result in order_list]
    return json.dumps(order_dict, default=str)

@app.route("/hotel-index")
def hotel_index():
    # log('enter hotel page')
    # order_list = Order.query.all()
    return render_template("hotel-index.html", list=[{}, {}, {}])

@app.route("/hotel-order")
def hotel_order():
    return render_template("hotel-order.html")

@app.route("/hotel-payment")
def hotel_payment():
    return render_template("hotel-payment.html")

@app.route("/hotel-payment-success")
def hotel_payment_success():
    return render_template("hotel-payment-success.html")


@app.route("/order-list")
def order_list():
    return render_template("order-list.html", list=[{}, {}], order_state={})