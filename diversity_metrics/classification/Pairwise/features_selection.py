import numpy as np
from itertools import combinations
from .pairwise_metrics import *


class FeatureSelection():
    """
    Abstract base class for pairwise classification diversity metrics.
    This class defines the basic structure for pairwise classification metrics.
    
    """
    def __init__(self,y,y_true,treeshold):
        """
        This a class that process the different mesures of the data features pair to pair and computes the diveristy metric and then remove the pair features that are below the treshold
        """
        self.threshold = treeshold

        self.y = [np.array(pred) for pred in y]
        self.y_true = np.array(y_true)
        self._validate_inputs()

    def _validate_inputs(self):
        """
        Check if all prediction arrays have the same length and match the length of y_true.
        """
        pred_length = len(self.y[0])
        for pred in self.y:
            if len(pred) != pred_length:
                raise ValueError("All prediction arrays must have the same length.")
        
        if len(self.y_true) != pred_length:
            raise ValueError("y_true must have the same length as each prediction array.")

    def calculate(self, metric_class='QStatistics'):
        """
        Computes the pairwise diversity metrics and filters out columns below the threshold.

        Args:
        metric_class (PairwiseClassificationMetric): A metric class for computing diversity.

        Returns:
        list: List of column indices that meet the threshold.
        """
        num_features = len(self.y)
        valid_columns = set(range(num_features))
        
        
        print("process begin") 

        if metric_class == 'QStatistics':
            if self.threshold > 1 or self.threshold < -1:
                raise ValueError("Threshold must be between -1 and 1 for QStatistics")

            # Compute pairwise metrics for all combinations of columns
            for i, j in combinations(range(num_features), 2):
                metric_instance= QStatistics(self.y[i], self.y[j], self.y_true)
                diversity_score = metric_instance.calculate()
                
                print(f"diversity_score between {i} and {j} ",diversity_score)
                # If diversity is below threshold, remove both columns from valid set
                if diversity_score > self.threshold:
                    valid_columns.discard(i)
                    valid_columns.discard(j)



        elif metric_class =='DifferencesMeasure':
            if self.threshold > 1 or self.threshold < 0:
                raise ValueError("Threshold must be between 0 and 1 for DifferencesMeasure")
            # Compute pairwise metrics for all combinations of columns
            for i, j in combinations(range(num_features), 2):
                metric_instance= DifferencesMeasure(self.y[i], self.y[j], self.y_true)
                diversity_score = metric_instance.calculate()
                
                print(f"diversity_score between {i} and {j} ",diversity_score)
                # If diversity is below threshold, remove both columns from valid set
                if diversity_score > self.threshold:
                    valid_columns.discard(i)
                    valid_columns.discard(j)

             
        elif metric_class =='CorrelationCoefficient':
            if self.threshold > 1 or self.threshold < -1:
                raise ValueError("Threshold must be between -1 and 1 for CorrelationCoefficient")
            # Compute pairwise metrics for all combinations of columns
            for i, j in combinations(range(num_features), 2):
                metric_instance= CorrelationCoefficient(self.y[i], self.y[j], self.y_true)
                diversity_score = metric_instance.calculate()
                
                print(f"diversity_score between {i} and {j} ",diversity_score)
                # If diversity is below threshold, remove both columns from valid set
                if diversity_score > self.threshold:
                    valid_columns.discard(i)
                    valid_columns.discard(j)

        elif metric_class =='DoubleFaultMeasure':
            if self.threshold > 1 or self.threshold < 0:
                raise ValueError("Threshold must be between 0 and 1 for DoubleFaultMeasure")
            # Compute pairwise metrics for all combinations of columns
            for i, j in combinations(range(num_features), 2):
                metric_instance= DoubleFaultMeasure(self.y[i], self.y[j], self.y_true)
                diversity_score = metric_instance.calculate()
                
                print(f"diversity_score between {i} and {j} ",diversity_score)
                # If diversity is below threshold, remove both columns from valid set
                if diversity_score > self.threshold:
                    valid_columns.discard(i)
                    valid_columns.discard(j)

        elif metric_class =='CombinationD_DF':
            if self.threshold > 1 or self.threshold < 0:
                raise ValueError("Threshold must be between -1 and 1 for CombinationD_DF")
            for i, j in combinations(range(num_features), 2):
                metric_instance= CombinationD_DF(self.y[i], self.y[j], self.y_true)
                diversity_score = metric_instance.calculate()
                
                print(f"diversity_score between {i} and {j} ",diversity_score)
                # If diversity is below threshold, remove both columns from valid set
                if diversity_score > self.threshold:
                    valid_columns.discard(i)
                    valid_columns.discard(j)

        else:
            raise ValueError("Invalid metric class")           
        
        
        # Return the remaining valid column indices
        return [str(idx) for idx in sorted(valid_columns)]