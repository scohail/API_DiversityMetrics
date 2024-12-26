# diversity_metrics/regression/base_metric.py

from abc import ABC, abstractmethod
import numpy as np

class NonPairwiseRegressionMetric(ABC):
    """
    Abstract base class for non-pairwise regression diversity metrics.
    """

    def __init__(self, predictions, y_true=None):
        """
        Initialize the non-pairwise regression metric with multiple predictions and optional true values.

        Parameters:
        predictions (list of array-like): A list of arrays, each representing predictions from one regressor
                                          across all data points.
        y_true (array-like, optional): True target values for supervised metrics.
        """
        self.predictions = [np.array(pred) for pred in predictions]
        self.y_true = np.array(y_true) if y_true is not None else None
        self._validate_inputs()

    def _validate_inputs(self):
        """
        Check if all prediction arrays have the same length and, if provided, match the length of y_true.
        """
        # Ensure all prediction arrays have the same length
        pred_length = len(self.predictions[0])
        for pred in self.predictions:
            if len(pred) != pred_length:
                raise ValueError("All prediction arrays must have the same length.")
        
        # Check that y_true matches the length of the predictions
        if self.y_true is not None and len(self.y_true) != pred_length:
            raise ValueError("y_true must have the same length as each prediction array.")

    @abstractmethod
    def calculate(self):
        """
        Calculate the metric value. Must be implemented in subclasses.
        """
        pass
