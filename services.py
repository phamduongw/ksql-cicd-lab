import requests
import json
from utils import get_base64_credentials


def apply(url, username, password, script):
    try:
        headers = {
            "Authorization": f"Basic {get_base64_credentials(username, password)}",
            "Content-Type": "application/json",
        }
        payload = json.dumps({"ksql": script})
        response = requests.post(url, headers=headers, data=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
