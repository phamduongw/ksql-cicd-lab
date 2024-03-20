import base64


def read_file_content(path):
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None  # Trả về None nếu tệp không tồn tại


def get_base64_credentials(username, password):
    try:
        credentials = f"{username}:{password}"
        credentials_bytes = credentials.encode("utf-8")
        base64_credentials = base64.b64encode(credentials_bytes).decode("utf-8")
        return base64_credentials
    except Exception as e:
        print(f"Error encoding credentials: {e}")
        return None  # Trả về None nếu có lỗi xảy ra trong quá trình mã hóa
