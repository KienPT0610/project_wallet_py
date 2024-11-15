from wallet.account import Account
from wallet.token import Token

class Wallet:
    def __init__(self):
        self.account = None
        self.token = None
    
    def login(self, private_key):
        try:
            self.account = Account(private_key)
        except Exception as e:
            print("Error: ", e)
    
    def create_account(self):
        self.account = Account()

    def logout(self):
        self.account = None
        self.token = None

    def load_wallet(self):
        if self.account is not None:
            self.token = Token(self.account.address)
        else:
            print("Please login first")
    