from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    direction = request.args.get('direction')
    # if current_user
    if not current_user.is_authenticated:
        return render_template('login.html', direction=direction)
    elif direction:
        return redirect(direction + f'?user_id={current_user.id}&user_name={current_user.name}&user_email={current_user.email}')
    else:
        return redirect(url_for('main.index'))


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    direction = request.form.get('direction')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)

    if direction != 'None':
        return redirect(direction + f'?user_id={user.id}&user_name={user.name}&user_email={user.email}')
    else:
        return redirect(url_for('main.index'))
  

@auth.route('/signup')
def signup():
    return render_template('signup.html')
  

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    new_user = User(email=email, name=name, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))