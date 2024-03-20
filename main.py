import os
import re
import sys
import logging

from utils import read_file_content
from services import apply

KSQLDB_URL = sys.argv[1]
KSQLDB_USERNAME = sys.argv[2]
KSQLDB_PASSWORD = sys.argv[3]
LOGS_FOLDER = sys.argv[4]
DIFF_FILENAMES = sys.argv[5].split("\n")

SCRIPT_FILENAMES_PATTERN = r"^scripts\/\w+\.sql$"

if __name__ == "__main__":
    # Log configuration
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)
    logging.basicConfig(
        filename=f"{LOGS_FOLDER}/ksql.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Filter the changed script and apply to ksqlDB
    for filename in DIFF_FILENAMES:
        if re.match(SCRIPT_FILENAMES_PATTERN, filename):
            script = read_file_content(filename)

            response = apply(
                KSQLDB_URL,
                KSQLDB_USERNAME,
                KSQLDB_PASSWORD,
                script,
            )

            if type(response) == list:
                for item in response:
                    logging.info(item["commandStatus"]["message"])

            elif type(response) == dict:
                logging.error(response["message"])
