import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s : %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log") #creating logfile 
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), #to save the logs in file
        logging.StreamHandler(sys.stdout) #to print the logs in console as well as in file
    ]  


)

logger = logging.getLogger("ML_Project")