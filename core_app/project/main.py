from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from .models import Module

main = Blueprint('main', __name__)

@main.route('/')
def index():
    list = Module.query.all()
    online_list = filter(lambda item: item.online, list)
    sorted_list = sorted(online_list, key=lambda x: x.index)
    username = current_user.name if current_user.is_authenticated else None

    return render_template('index.html', list=sorted_list, username=username)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


########################## Internal ###################################

@main.route('/internal/register', methods=['POST'])
def register_module():
    index = request.json.get('index')
    name = request.json.get('name')
    url = request.json.get('url')
    photo = request.json.get('photo')
    authorization = request.json.get('authorization')
    
    module = Module.query.filter_by(index=index).first()
    if module:
        module.name = name
        module.url = url
        module.photo = photo
        module.authorization = authorization
        module.online = True
        module.time = datetime.now().timestamp()
        db.session.commit()
    else:
        module = Module(index=index, name=name, url=url, photo=photo, authorization=authorization, online=True, time=datetime.now().timestamp())
        db.session.add(module)
        db.session.commit()
    
    return f'register {name} success!'

@main.route('/internal/unload', methods=['GET'])
def unload_module():
    index = request.args.get('index')
    module = Module.query.filter_by(index=index).first()
    if module:
        module.online = False
        db.session.commit()
        return f' unload {module.name} success!'
    else:
        return f'Do not find the {index} module'