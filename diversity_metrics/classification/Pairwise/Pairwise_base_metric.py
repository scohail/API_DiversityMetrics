from abc import ABC, abstractmethod
import numpy as np

class PairwiseClassificationMetric(ABC):
    """
    Abstract base class for pairwise classification diversity metrics.
    This class defines the basic structure for pairwise classification metrics.
    """

    def __init__(self, y_1, y_2, y_true):
        """
        Initialize the pairwise classification metric with predictions from two classifiers and optional true labels.

        Parameters:
        y_1 (array-like): Predictions from the first classifier across all data points.
        y_2 (array-like): Predictions from the second classifier across all data points.
        y_true (array-like, optional): True target values.
        """
        self.y_1 = np.array(y_1)
        self.y_2 = np.array(y_2)
        self.y_true = np.array(y_true)
        self._validate_inputs()


    def _validate_inputs(self):
        """
        Check if prediction arrays have the same length and, if provided, match the length of y_true.
        """
        pred_length = len(self.y_1)

        

        
        if len(self.y_2) != pred_length:
            raise ValueError("Both prediction arrays must have the same length.")
        
        if len(self.y_true) != pred_length:
            raise ValueError("y_true must have the same length as each prediction array.")
        
        
        

    def _binary_counts(self):
        """
        Calculate the counts of true positives (a), false positives (b),
        false negatives (c), and true negatives (d) for a binary classification.

        Parameters:
        y_pred (array-like): Predicted target values for binary classification.

        Returns:
        tuple: Counts of (a, b, c, d).
        """
    
        a = np.sum((self.y_true == self.y_1) & (self.y_true == self.y_2))
        b = np.sum((self.y_true == self.y_1) & (self.y_true != self.y_2))
        c = np.sum((self.y_true != self.y_1) & (self.y_true == self.y_2))
        d = np.sum((self.y_true != self.y_1) & (self.y_true != self.y_2))

        return a, b, c, d
    

    @abstractmethod
    def calculate(self):
        """
        Calculate the metric value. Must be implemented in subclasses.
        """
        pass