from wallet.account import Account
from wallet.token import Token

class Wallet:
    def __init__(self):
        self.account = None
        self.token = None
    
    def login(self, private_key):
        try:
            self.account = Account(private_key)
            self.load_wallet()
        except Exception as e:
            print("Error: ", e)
    
    def create_account(self):
        self.account = Account()
        self.load_wallet()

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
    