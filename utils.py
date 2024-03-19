import os
import base64


def read_file_content(path):
    with open(path, "r") as file:
        return file.read()


def list_filenames(path):
    return os.listdir(path)


def write_to_file(path, content):
    with open(path, "a") as file:
        file.write(content + "\n")


def getBase64Credentials(username, password):
    credentials = f"{username}:{password}"
    credentials_bytes = credentials.encode("utf-8")
    base64_credentials = base64.b64encode(credentials_bytes).decode("utf-8")
    return base64_credentials
