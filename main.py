import re
import sys
import logging
from pathlib import Path
from utils import read_file_content
from services import apply

KSQLDB_URL, KSQLDB_USERNAME, KSQLDB_PASSWORD, LOGS_FOLDER, *DIFF_FILENAMES = sys.argv[
    1:
]
SCRIPT_FILENAMES_PATTERN = r"^scripts\/.+\.sql$"


def main():
    # Log configuration
    Path(LOGS_FOLDER).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=f"{LOGS_FOLDER}/ksql.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Filter the changed script and apply to ksqlDB
    for filename in DIFF_FILENAMES:
        if re.match(SCRIPT_FILENAMES_PATTERN, filename):
            response = apply(
                KSQLDB_URL,
                KSQLDB_USERNAME,
                KSQLDB_PASSWORD,
                read_file_content(filename),
            )

            if isinstance(response, list):
                for item in response:
                    logging.info(item["commandStatus"]["message"])
            elif isinstance(response, dict):
                logging.error(response["message"])


if __name__ == "__main__":
    main()
