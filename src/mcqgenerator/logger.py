import logging
import os
from datetime import datetime
# File name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# os.path.join(os.getcwd(), "logs"): os.getcwd() - Returns the current working directory and combines the current working directory with the "logs" directory name to form a full path for where the log files will be stored.
log_path = os.path.join(os.getcwd(), "logs")

# os.makedirs(log_path, exist_ok=True): Creates the "logs" directory if it doesn't already exist. The exist_ok=True argument prevents an error if the directory already exists
os.makedirs(log_path, exist_ok=True)

#os.path.join(log_path, LOG_FILE): Combines the log_path (directory) with the LOG_FILE (file name) to form the complete path to the log file.
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

#filename=LOG_FILEPATH: Specifies that the log messages should be written to the file located at LOG_FILEPATH.
logging.basicConfig(filename=LOG_FILEPATH,
                    level=logging.INFO,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )
