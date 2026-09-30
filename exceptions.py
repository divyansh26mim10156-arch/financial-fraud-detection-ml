class FraudDetectionException(Exception):
    """Base exception for the fraud detection system."""
    pass

class DataLoadingError(FraudDetectionException):
    """Raised when the dataset cannot be loaded or is corrupted."""
    pass

class ModelTrainingError(FraudDetectionException):
    """Raised when the ML model fails to train or converge."""
    pass
