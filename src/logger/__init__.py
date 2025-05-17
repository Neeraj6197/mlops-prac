import logging
from datetime import datetime
import os
import sys
from logging.handlers import RotatingFileHandler #for oversized files

#log configuration:
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('m%_d%_Y%_%H_%M_%S')}.log"
MAX_LOG_SIZE = 20 * 1024 * 1024  # 20 MB

#constructing log folder:
log_dir_path = "./logs"
os.makedirs(log_dir_path, exist_ok=True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

#configure the logger function:
def configure_logger():
    """
    Configures logging with a rotating file handler and a console handler.
    """
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Define formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=3,
                                        encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()