import os
import sys
import logging

from utils import read_file_content, list_filenames
from services import apply

KSQLDB_URL = sys.argv[1]
KSQLDB_USERNAME = sys.argv[2]
KSQLDB_PASSWORD = sys.argv[3]

APPLY_SCRIPTS_FOLDER = "scripts/apply"
LOGS_FOLDER = "logs"

if __name__ == "__main__":
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)

    logging.basicConfig(
        filename=f"{LOGS_FOLDER}/ksql.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    for filename in list_filenames(APPLY_SCRIPTS_FOLDER):
        script = read_file_content(f"{APPLY_SCRIPTS_FOLDER}/{filename}")
        response = apply(
            KSQLDB_URL,
            KSQLDB_USERNAME,
            KSQLDB_PASSWORD,
            script,
        )
        if type(response) == list:
            logging.info(response[0]["commandStatus"]["message"])
        elif type(response) == dict:
            logging.error(response["message"])
