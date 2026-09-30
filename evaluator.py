from sklearn.metrics import classification_report, confusion_matrix
from logger_config import setup_logger

logger = setup_logger()

class ModelEvaluator:
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def generate_report(self):
        logger.info("Generating performance evaluation metrics...")
        cm = confusion_matrix(self.y_true, self.y_pred)
        report = classification_report(self.y_true, self.y_pred)
        
        print("=== Confusion Matrix ===")
        print(cm)
        print("\n=== Classification Report ===")
        print(report)
        
        logger.info("Evaluation metrics generated successfully.")
        return cm, report
