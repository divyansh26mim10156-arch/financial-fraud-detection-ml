import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from logger_config import setup_logger

logger = setup_logger()

class DataPreprocessor:
    def __init__(self, df: pd.DataFrame, target_column: str):
        self.df = df
        self.target_column = target_column

    def process(self, test_size=0.2):
        logger.info("Starting data preprocessing pipeline...")
        X = self.df.drop(columns=[self.target_column])
        y = self.df[self.target_column]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=test_size, random_state=42, stratify=y
        )
        logger.info("Preprocessing complete. Train/Test split generated successfully.")
        return X_train, X_test, y_train, y_test
