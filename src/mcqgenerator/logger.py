'''
Below script creates a log file in a "logs" directory, names it with a timestamp, and
configures the logging module to write messages to this file with detailed information about each log entry.
'''

import logging # To configure logging
import os # To work with Operating system
from datetime import datetime # working with dates and times

# log file name with a timestamp
LOG_FILE=f"{datetime.now().strftime('%m_%d-%Y_%H_%M_%S')}.log"

# Constructs the full path by joining the current working directory
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) # to create the (logs) folder

# The full path to the log file
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Basic configuration for the logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # log message format
    level=logging.INFO
)