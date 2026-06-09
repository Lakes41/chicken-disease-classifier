import os
import logging
import sys

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

log_dir = 'logs'
log_path = os.path.join(log_dir, "cnnClassifier.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(level=logging.INFO,
                    format=log_fmt,
                    handlers=[
                        logging.FileHandler(log_path),
                        logging.StreamHandler(sys.stdout)
                    ]
                    )

logger = logging.getLogger("cnnClassifier")