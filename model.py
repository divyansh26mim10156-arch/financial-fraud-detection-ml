from sklearn.ensemble import RandomForestClassifier
from exceptions import ModelTrainingError
from logger_config import setup_logger

logger = setup_logger()

class FraudClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)

    def train(self, X_train, y_train):
        try:
            logger.info("Training Random Forest Classifier model...")
            self.model.fit(X_train, y_train)
            logger.info("Model training completed successfully.")
        except Exception as e:
            logger.error(f"Model training failed: {str(e)}")
            raise ModelTrainingError(f"Error during model training: {e}")

    def predict(self, X_test):
        logger.info("Generating predictions on test dataset...")
        return self.model.predict(X_test)
