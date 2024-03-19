import requests
import json

from utils import getBase64Credentials


def apply(url, username, password, script):
    headers = {
        "Authorization": f"Basic {getBase64Credentials(username, password)}",
        "Content-Type": "application/json",
    }

    query = {"ksql": script}

    payload = json.dumps(query)

    response = requests.post(url, headers=headers, data=payload)
    return response.json()
