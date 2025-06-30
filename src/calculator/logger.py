import logging
import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
LOG_FORMAT = os.getenv('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG_FILE = os.getenv('LOG_FILE', '').strip()

# Create logger
logger = logging.getLogger('AdvancedCalculator')
logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

formatter = logging.Formatter(LOG_FORMAT)

if LOG_FILE:
    handler = logging.FileHandler(LOG_FILE)
else:
    handler = logging.StreamHandler()

handler.setFormatter(formatter)
logger.addHandler(handler)
