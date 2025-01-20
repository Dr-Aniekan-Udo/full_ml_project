import logging
import os
from datetime import datetime

'''
This file will store logging information 
and error information  such as time, date, etc
so that it could be revisited
'''
# Create template for log file
# All the log file will end with .log

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"

# assign a path for the log file
# all log file will begin with logs, then follwed by our template

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# the above code will join 'logs' string and log file template with respect to the current working directory

# append files to folder or make new one if if does not existed

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
