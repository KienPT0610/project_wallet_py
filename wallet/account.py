from wallet.provider import Provider
from config.settings import API_URL

class Account:
    def __init__(self, private_key=None):
        provider = Provider(API_URL)
        if private_key is None:
            self.account = provider.create_account()
        else:
            self.account = provider.get_account(private_key)

    @property
    def address(self):
        return self.account.address
    
    @property
    def private_key(self):
        return self.account.key.hex()
    
    def sign_transaction(self, transaction):
        return self.account.sign_transaction(transaction, self.private_key)
    