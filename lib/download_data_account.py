from flask import *
import tempfile

def generate_txt(username, password, address, private_key):
    """
    Tạo file TXT chứa thông tin người dùng.

    Args:
        username (str): Tên người dùng.
        password (str): Mật khẩu.
        address (str): Địa chỉ ví.
        private_key (str): Khóa riêng.

    Returns:
        str: Đường dẫn tới file TXT đã tạo.
    """
    # Tạo thư mục tạm thời và tệp TXT
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as file:
        file.write("User Information\n")
        file.write("-----------------\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Private Key: {private_key}\n")

        # Trả về đường dẫn tới tệp đã tạo
        return file.name