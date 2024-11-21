
from wallet.provider import Provider
from config.settings import API_URL, CONTRACT_USERS_ADDRESS, CONTRACT_USERS_ABI

class Users:
    def __init__(self):
        self.provider = Provider(API_URL)
        self.w3 = self.provider.get_web3()
        self.contract = self.w3.eth.contract(address=CONTRACT_USERS_ADDRESS, abi=CONTRACT_USERS_ABI)


    def get_user_name(self, private_key=None):
        return self.contract.functions.get_user_name(private_key).call()
    
    def forgot_password(self, username=None, password=None):
        try:
            return self.contract.functions.forgot_password(username, password).call()
        except Exception as error:
            return None
    
    def is_created(self, username):
        return self.contract.functions.isCreated(username).call()

    def create_user(self, username, password, private_key):
        private_key_ad = "d36d4cd541314811bb9e1f3e37c2a6370adde8fb8d8d3aaab3fb624c5156dcc6"
        account = self.provider.get_web3().eth.account.from_key(private_key_ad)
        tx = self.contract.functions.create_user(username, password, private_key).build_transaction(self.provider.transaction_config(account.address))
        signed_tx = self.provider.get_web3().eth.account.sign_transaction(tx, private_key=private_key_ad)
        tx_hash = self.provider.get_web3().eth.send_raw_transaction(signed_tx.raw_transaction)
        return tx_hash