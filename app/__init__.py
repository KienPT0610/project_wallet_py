from flask import Flask
from app.routes import *

def create_app():
    app = Flask(__name__)

    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/create_account', 'create-account', create_account, methods=['POST'])
    app.add_url_rule('/login_account', 'login-account', login_account, methods=['POST'])
    
    app.add_url_rule('/account/<address>', 'account', account)
    app.add_url_rule('/send', 'send', send)
    app.add_url_rule('/receive', 'receive', receive)
    # app.add_url_rule('/logout', 'logout', logout)

    app.add_url_rule('/get_account_address', 'get-account-address', get_account_address)
    app.add_url_rule('/transactions', 'transactions', transactions)

    return app
