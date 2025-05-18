import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)     

    CORS(app, resources={r"/*":{'origins':"*"}})
    CORS(app, resources={r"/*": {"origins": 'http://localhost:8080', "allow_headers": ["Content-Type", "X-CSRF-Token", "Access-Control-Allow-Origin"]}})
    
    # Database
    db.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    
    return app
