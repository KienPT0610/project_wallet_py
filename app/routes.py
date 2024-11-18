from flask import *
from wallet.wallet import Wallet
from lib.download_data_account import generate_txt

wallet = Wallet()

def index():
    return render_template('index.html')

def create_account():
    username = request.form.get('username')
    password = request.form.get('password')
    result = wallet.create_account(username=username, password=password)
    if result is None:
        return render_template('index.html', address="", error="Username already exists")
    address, private_key = result 
    # Tạo file TXT
    txt_path = generate_txt(username, password, address, private_key)

    # Gửi tệp TXT để tải xuống
    return send_file(
        txt_path,
        as_attachment=True,
        download_name=f"user_info_{username}.txt",
        mimetype='text/plain'
    )

def login_account():
    print("login_account")  
    pivate_key = request.form.get('private_key')
    result = wallet.login(private_key=pivate_key)
    if result is None:
        return render_template('index.html', address="", error="Invalid private key")
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
    wallet.load_wallet()
    return render_template('send.html', account=wallet.account)

def receive():
    wallet.load_wallet()
    return render_template('receive.html', account=wallet.account)

def transactions():
    send_transactions = wallet.token.get_send_transactions()
    receive_transactions = wallet.token.get_receive_transactions()
    wallet.load_wallet()
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
    
def forgot_password():
    return render_template('forgot_password.html')
    
def get_password():
    username = request.form.get('username')
    passkey = request.form.get('passkey')
    private_key = wallet.forgot_password(username, passkey)
    if private_key is None:
        return render_template('forgot_password.html', error="Invalid username or passkey || Username does not exist")
    txt_path = generate_txt(username, passkey, "", private_key)
    # Gửi tệp TXT để tải xuống
    return send_file(
        txt_path,
        as_attachment=True,
        download_name=f"user_info_{username}.txt",
        mimetype='text/plain'
    )

def logout():
    wallet.logout()
    return redirect(url_for('index'))