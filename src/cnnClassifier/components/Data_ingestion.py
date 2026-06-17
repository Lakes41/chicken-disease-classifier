import os
import kagglehub
from cnnClassifier import logger
from cnnClassifier.entities.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import get_folder_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from {self.config.handler}")
            
            kagglehub.dataset_download(self.config.handler, output_dir = self.config.root_dir)
            logger.info(f"Downloaded file to {self.config.local_data_file}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file} {get_folder_size(self.config.local_data_file)} bytes)")
