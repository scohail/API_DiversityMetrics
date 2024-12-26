from abc import ABC, abstractmethod
import numpy as np



class PairwiseRegressionMetric(ABC):
    """
    Abstract base class for regression diversity metrics.
    """

    def __init__(self, y1, y2, y_true=None, threshold=None):
        """
        Initialize the regression metric with the predictions and optional parameters.

        Parameters:
        y1 (array-like): Predictions from the first regressor.
        y2 (array-like): Predictions from the second regressor.
        y_true (array-like, optional): True target values for supervised metrics.
        threshold (float, optional): Threshold for metrics that require a decision boundary.
        """
        self.y1 = np.array(y1)
        self.y2 = np.array(y2)
        self.y_true = np.array(y_true) if y_true is not None else None
        self.threshold = threshold
        self._validate_inputs()

    def _validate_inputs(self):
        """
        Check if the input arrays have the same length.
        """
        if len(self.y1) != len(self.y2):
            raise ValueError("y1 and y2 must have the same length.")
        if self.y_true is not None and len(self.y1) != len(self.y_true):
            raise ValueError("y1, y2, and y_true must have the same length when y_true is provided.")
    
    @abstractmethod
    def calculate(self):
        """
        Calculate the metric value. it's implemented in the subclasses.
        """
        pass
