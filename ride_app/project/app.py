from flask import Blueprint, current_app, session, request, render_template, redirect, url_for, jsonify
from datetime import datetime
from .objects import Order, OrderBill, OrderEnum
from . import db

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
@app.route("/")
def index():
    if request.args.get('user_id'):
        session['user_id'] = request.args.get('user_id')
        session['user_name'] = request.args.get('user_name')
        session['user_email'] = request.args.get('user_email')

    return redirect(url_for('app.ride')) # <--- rename to module's index name


@app.route("/ride")
def ride():
    log('enter ride page')
    return render_template("ride.html")


@app.route("/ride/route", methods=["GET"])
def ride_route():
    loc = request.args.get("location", "")
    dest = request.args.get("destination", "")
    context = {
        "location": loc,
        "destination": dest,
        "routes": [
            {"id": 1, "name": f"{loc} to {dest} route A", "price": 10},
            {"id": 2, "name": f"{loc} to {dest} route B", "price": 20},
            {"id": 3, "name": f"{loc} to {dest} route C", "price": 30},
        ],
    }
    log('request route planning')
    return render_template("ride_route.html", **context)


@app.route("/ride/order", methods=["POST"])
def ride_order():
    name =  request.form.get('name', '')
    price =  request.form.get('price', '')
    user_id = getUser()[0]
    
    order = Order(user_id=user_id, name=name, price=price, state=OrderEnum.INIT.value, datetime=datetime.now().timestamp())
    db.session.add(order)
    db.session.commit()
    log('create ride order')
    
    order_bill = OrderBill(order_id=order.id, has_pay=False, datetime=datetime.now().timestamp())
    db.session.add(order_bill)
    db.session.commit()
    log('create ride order bill')
    
    return { 'order_id': order.id }

@app.route('/ride/payment')
def ride_payment():
    id = request.args.get('id')
    
    order = Order.query.filter_by(id=id).first()
    order_bill = OrderBill.query.filter_by(order_id=order.id).first()
    order_state = { state.value: state.name.lower() for state in OrderEnum}
    
    return render_template('ride_payment.html', order=order, order_bill=order_bill, order_state=order_state)

@app.route('/ride/location')
def ride_location():
    return render_template('ride_location.html')

@app.route('/ride/onboard')
def ride_onboard():
    return render_template('ride_onboard.html')

@app.route('/ride/complete')
def ride_complete():
    return render_template('ride_complete.html')

@app.route('/ride/order_pay', methods=['GET'])
def order_pay():
    id = request.args.get('id')
    
    order = Order.query.filter_by(id=id).first()
    order_bill = OrderBill.query.filter_by(order_id=order.id).first()
    
    # Overdue for payment
    if order.datetime + 3600 < datetime.now().timestamp():
        order.state = OrderEnum.INVAILD.value
        db.session.commit()
        return 'Order had been invaild'
    
    order.state = OrderEnum.PAID.value
    order_bill.has_pay = True
    order_bill.datetime = datetime.now()
    db.session.commit()
    log('Pay ride order bill')
    
    return 'Pay order success'

@app.route('/ride/order_delete', methods=['DELETE'])
def order_delete():
    id = request.args.get('id')
    
    order = Order.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()
    log('Delete ride order')
    
    return 'Delete order success'

@app.route('/ride/order_list')
def order_list():
    id, name, email = getUser()
    user = { 'id': id, 'name': name}
    
    list = Order.query.filter_by(user_id=id)
    for item in list:
        item.datestr = datetime.fromtimestamp(item.datetime).strftime('%Y-%m-%d %H:%M:%S')
    
    order_state = { state.value: state.name.lower() for state in OrderEnum}
    log('Request ride order list')
    
    return render_template('order_list.html', user=user, list=list, order_state=order_state)

@app.route('/ride/order_close', methods=['GET'])
def order_close():
    id = request.args.get('id')
    
    order = Order.query.filter_by(id=id).first()
    order.state = OrderEnum.INVAILD.value
    db.session.commit()
    log('Close ride order')
    
    return 'Close order success'

@app.route('/ride/order_cancel', methods=['GET'])
def order_cancel():
    id = request.args.get('id')
    
    order = Order.query.filter_by(id=id).first()
    order.state = OrderEnum.CANCEL.value
    db.session.commit()
    log('Cancel ride order')
    
    return 'Cancel order success'

@app.route('/ride/order_onboard', methods=['GET'])
def order_onboard():
    id = request.args.get('id')
    
    order = Order.query.filter_by(id=id).first()
    order.state = OrderEnum.ONBOARD.value
    db.session.commit()
    log('Onboard ride order')
    return 'Ride service has start'

@app.route('/ride/order_complete', methods=['GET'])
def order_complete():
    id = request.args.get('id')
    
    order = Order.query.filter_by(id=id).first()
    order.state = OrderEnum.COMPLETE.value
    db.session.commit()
    log('Complete ride order')
    
    return 'Ride service has completed'