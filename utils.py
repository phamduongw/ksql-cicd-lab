import os
import base64


def read_file_content(path):
    with open(path, "r") as file:
        return file.read()


def get_base64_credentials(username, password):
    credentials = f"{username}:{password}"
    credentials_bytes = credentials.encode("utf-8")
    base64_credentials = base64.b64encode(credentials_bytes).decode("utf-8")
    return base64_credentials
