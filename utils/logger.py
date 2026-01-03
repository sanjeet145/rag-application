import datetime
import logging
import os 

filepath = 'log/'
os.makedirs(filepath,exist_ok=True)

log_file=os.path.join(filepath,f'{datetime.datetime.now().strftime("%Y%m%d")}.log') 

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%y %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)