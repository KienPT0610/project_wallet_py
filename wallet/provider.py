from web3 import Web3

class Provider:
    def __init__(self, api_url):
        # Khởi tạo kết nối đến blockchain với URL được cung cấp
        self.w3 = Web3(Web3.HTTPProvider(api_url))
        
        if not self.w3.is_connected():
            raise ConnectionError("Unable to connect to the blockchain network")
    
    def get_web3(self):
        # Trả về kết nối Web3 hiện tại để các lớp khác sử dụng
        return self.w3
    
    def create_account(self):
        # Tạo một tài khoản mới
        return self.w3.eth.account.create()
    
    def get_account(self, private_key):
        # Lấy tài khoản từ private key
        return self.w3.eth.account.from_key(private_key)
