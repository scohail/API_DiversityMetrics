from abc import ABC, abstractmethod
import numpy as np


class NonPairwiseClassificationMetric(ABC):
    """
    Abstract base class for non-pairwise classification diversity metrics.
    """

    def __init__(self, predictions, y_true):
        """
        Initialize the non-pairwise classification metric with multiple predictions and true labels.

        Parameters:
        predictions (list of array-like): A list of arrays, each representing predictions from one classifier
                                          across all data points.
        y_true (array-like): True target values.
        """
        self.predictions = [np.array(pred) for pred in predictions]
        self.y_true = np.array(y_true)
        self._validate_inputs()

    def _validate_inputs(self):
        """
        Check if all prediction arrays have the same length and match the length of y_true.
        """
        print("the metric of values ", self.predictions)
        print("the metric of true values ", self.y_true)

        pred_length = len(self.predictions[0])
        for pred in self.predictions:
            if len(pred) != pred_length:
                raise ValueError("All prediction arrays must have the same length.")
        
        if len(self.y_true) != pred_length:
            raise ValueError("y_true must have the same length as each prediction array.")


    @abstractmethod
    def calculate(self):
        """
        Calculate the metric value. Must be implemented in subclasses.
        """
        pass