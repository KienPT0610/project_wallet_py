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

def get_account_address():
    try:
        account_address = wallet.account.address
        return jsonify(account_address)
    except Exception as error:
        return jsonify({"error": str(error)})

def send():
    return render_template('send.html', account=wallet.account)

def receive():
    return render_template('receive.html', account=wallet.account)

def transactions():
    send_transactions = wallet.token.get_send_transactions()
    receive_transactions = wallet.token.get_receive_transactions()
    return render_template(
        'transactions.html', 
        send_transactions=send_transactions, 
        receive_transactions=receive_transactions
    )

def send_token():
    try:
        to = request.form.get('to')
        amount = request.form.get('amount')
        memo = request.form.get('memo')
        wallet.send_token(to, amount, memo)
        return redirect(url_for('transactions'))
    except Exception as error:
        return jsonify({"error": str(error)})
