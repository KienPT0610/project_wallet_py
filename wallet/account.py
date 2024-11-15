from wallet.provider import Provider
from config.settings import API_URL

class Account:
    def __init__(self, private_key=None):
        self.provider = Provider(API_URL)
        if private_key is None:
            self.account = self.provider.create_account()
        else:
            self.account = self.provider.get_account(private_key)

    @property
    def address(self):
        return self.account.address
    
    @property
    def private_key(self):
        return self.account.key.hex()
    
    @property
    def balance(self):
        return self._balance
    
    def set_balance(self, balance):
        self._balance = balance

    def sign_transaction(self, tx):
        signed_tx = self.provider.get_web3().eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.provider.get_web3().eth.send_raw_transaction(signed_tx.raw_transaction)
        return tx_hash
    
    