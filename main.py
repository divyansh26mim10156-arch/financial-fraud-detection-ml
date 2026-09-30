import sys
from data_loader import DataLoader
from preprocessor import DataPreprocessor
from model import FraudClassifier
from evaluator import ModelEvaluator
from logger_config import setup_logger

logger = setup_logger()

def main():
    logger.info("Application started.")
    print("[*] Initializing Fraud Detection System...")
    
    dataset_path = r"D:\MyPythonProject\fraud\creditcard_sample.csv"
    
    try:
        loader = DataLoader(dataset_path)
        df = loader.load_data()
        
        preprocessor = DataPreprocessor(df, target_column="Class")
        X_train, X_test, y_train, y_test = preprocessor.process()
        
        classifier = FraudClassifier()
        classifier.train(X_train, y_train)
        
        predictions = classifier.predict(X_test)
        
        evaluator = ModelEvaluator(y_test, predictions)
        evaluator.generate_report()
        
        print("[+] Execution finished successfully. Check logs/system.log for details.")
    except Exception as e:
        logger.critical(f"Critical system failure: {str(e)}")
        print(f"[!] Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
