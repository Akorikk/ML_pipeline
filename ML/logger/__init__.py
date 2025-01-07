import logging 
import os, sys 
from datetime import datetime

LOG = "logs"
LOG = os.path.join(os.getcwd(), LOG)

os.makedirs(LOG, exist_ok=True)

current = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"Log{current}"


log_file = os.path.join(LOG, file_name)

logging.basicConfig(
    filename= log_file,
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level= logging.INFO
)