import pandas as pd
from exceptions import DataLoadingError
from logger_config import setup_logger

logger = setup_logger()

class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_data(self) -> pd.DataFrame:
        try:
            logger.info(f"Attempting to load dataset from {self.filepath}")
            df = pd.read_csv(self.filepath)
            logger.info(f"Dataset successfully loaded with shape: {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Failed to load dataset: {str(e)}")
            raise DataLoadingError(f"Could not load data from {self.filepath}: {e}")
