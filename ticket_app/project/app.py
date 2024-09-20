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
    return redirect(url_for('app.test')) # <--- rename to module's index name

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