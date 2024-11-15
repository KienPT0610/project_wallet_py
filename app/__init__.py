from flask import Flask
from app.routes import *

def create_app():
    app = Flask(__name__)

    app.add_url_rule('/', 'index', index)

    return app
