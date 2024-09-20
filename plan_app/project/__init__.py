from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
import requests
import json

# configuration
logging.basicConfig(
    filename='info.log', 
    format='%(asctime)s, %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'tourism secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)
    
    # blueprint for routes in our app
    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)
    
    # init database
    with app.app_context():
        db.create_all()
      
    # register application
    with open("project/config.json", "r") as config_file:
        config_data = json.load(config_file)
        register_url = config_data.get("register")
        try:
            res = requests.post(register_url, json=config_data)
            print(res.text)
        except:
            print(f'❌fail to register this module to core app')  
        print('Module is running:', config_data.get('url'))

    return app