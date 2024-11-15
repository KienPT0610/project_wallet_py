from flask import *
from wallet.wallet import Wallet

wallet = Wallet()

def index():
    return render_template('index.html')

def create_account():
    wallet.create_account()
    print(wallet.account.private_key)
    return "Account created"

def login_account():
    print("login_account")  
    pivate_key = request.form.get('private_key')
    wallet.login(private_key=pivate_key)
    return redirect(url_for('account', address=wallet.account.address))

def account(address):
    account = wallet.account
    return render_template('wallet.html', account=account)

def send():
    return render_template('send.html', account=wallet.account)