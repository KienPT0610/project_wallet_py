from web3 import Web3
from wallet.provider import Provider
from config.settings import API_URL, CONTRACT_ABI, CONTRACT_ADDRESS


class Token:
    def __init__(self, default_account):
        self.provider = Provider(API_URL)
        self.w3 = self.provider.get_web3()
        self.address = CONTRACT_ADDRESS
        self.default_account = default_account
        self.contract = self.w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
    
    @property
    def name(self):
        return self.contract.functions.name().call()
    
    @property
    def symbol(self):
        return self.contract.functions.symbol().call()
    
    @property
    def decimals(self):
        return self.contract.functions.decimals().call()
    
    @property
    def total_supply(self):
        return self.contract.functions.totalSupply().call()
    
    def balance_of(self, account=None):
        if account is None:
            account = self.default_account
        balance = self.contract.functions.balanceOf(account).call()
        return self.w3.from_wei(balance, 'ether')
    
    def allowance(self, owner=None, spender=None):
        if owner is None:
            owner = self.default_account
        if spender is None:
            spender = self.address
        return self.contract.functions.allowance(owner, spender).call()
    
    def get_send_transactions(self):
        return self.contract.functions.getSendTransactions(self.default_account).call()
    
    def get_receive_transactions(self):
        return self.contract.functions.getReceiveTransactions(self.default_account).call()
    
    def create_transaction_send_token(self, to, amount, memo):
        amount_wei = self.w3.to_wei(amount, 'ether')
        tx = self.contract.functions.sendToken(to, amount_wei, memo).build_transaction(self.provider.transaction_config(self.default_account))
        return tx

    

