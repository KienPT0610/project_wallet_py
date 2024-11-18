from wallet.account import Account
from wallet.token import Token
from wallet.users import Users

class Wallet:
    def __init__(self):
        self.account = None
        self.token = None
        self.users = None
        self.user_name = "name"
    
    def login(self, private_key):
        if private_key is None or len(private_key)!=64:
            return None
        self.account = Account(private_key)
        if self.account is None:
            return None
        self.load_wallet()
        return self.account

    
    def create_account(self, username, password):
        self.account = Account()
        self.users = Users()
        if self.users.is_created(username=username) == True:
            return None
        self.users.create_user(username, password, self.account.private_key)
        return self.account.address, self.account.private_key
    
    def forgot_password(self, username, password):
        self.users = Users()
        if self.users.is_created(username=username) == False:
            return None
        private_key = self.users.forgot_password(username, password)
        if private_key is None:
            return None
        return private_key     

    def logout(self):
        self.account = None
        self.token = None

    def load_wallet(self):
        if self.account is not None:
            self.token = Token(self.account.address)
            balance = self.token.balance_of()
            self.account.set_balance(balance=balance)
        else:
            print("Please login first")

    def send_token(self, to, amount, memo):
        tx = self.token.create_transaction_send_token(to, amount, memo)
        return self.account.sign_transaction(tx)