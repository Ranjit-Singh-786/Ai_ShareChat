import os,sys
import logging
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

#preparing path for log files
log_file_base_path = os.getenv("LOG_DIR_PATH")
log_directory = "shareChat_Logs"
log_directory_path = os.path.join(log_file_base_path,log_directory)
current_time_stamp = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = "log_"+current_time_stamp+".log"
#making Logging directory
os.makedirs(log_directory_path,exist_ok=True)

#joining logging Directory path with its filename
log_file_path = os.path.join(log_directory_path,file_name)

# Initializing logging instance
logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    level=logging.DEBUG,
                    format="[%(asctime)s]  - %(levelname)s - %(message)s")



