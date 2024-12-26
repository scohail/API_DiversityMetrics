# diversity_metrics/classification/__init__.py
from .NonPairwise_base_metric import NonPairwiseClassificationMetric
import numpy as np




class Entropy(NonPairwiseClassificationMetric):
    """
    Calculate the entropy of the ensemble predictions for a classification task.
    """
    def calculate(self):
        """
        Calculate the Entropy metric for multiple classifiers.

        Returns:
        float: The entropy value.
        """
        N = len(self.predictions[0])
        L = len(self.predictions)
        entropy_sum = 0

        print("the metric of values ", self.predictions)
        

        for i in range(N):
            sum_Yj = sum(1 if self.predictions[j][i] == self.y_true[i] else 0 for j in range(L))
            entropy_sum += min(sum_Yj, L - sum_Yj)
            print("Entropy sum: ", entropy_sum)

        entropy = (1 / N) * (2 /( L - 1)) * entropy_sum
        return entropy



class  KohaviWolpertVariance(NonPairwiseClassificationMetric):
    """
    measure the diversity of a compound set for binary classifiers.
    """
    def calculate(self):
        """
        Calculate the KohaPvi-Wolpert Variance metric for multiple classifiers.

        Returns:
        float: The Kohavi-Wolpert Variance value.
        """
        N = len(self.predictions[0])
        L = len(self.predictions)
        
        variance_sum = 0

        for i in range(N):
            sum_Yj = sum(1 if self.predictions[j][i] == self.y_true[i] else 0 for j in range(L))
            variance_sum += (sum_Yj * (L - sum_Yj)) 

        KW =  (1 / (N * L**2)) * variance_sum 

        return KW
    

class MeasurementInterraterAgreement(NonPairwiseClassificationMetric):
    """
    Calculate the the agreement level inside the classifiers set.
    """
    def calculate(self):
        """
        Calculate the Measurement Interrater Agreement metric for multiple classifiers.

        Returns:
        float: The Measurement Interrater Agreement value.
        """
        N = len(self.predictions[0])
        L = len(self.predictions)
        
        accuracy_sum = 0
        Yj=[]


        for i in range(N):
            sum_Yj = sum(1 if self.predictions[j][i] == self.y_true[i] else 0 for j in range(L))
            Yj.append(sum_Yj)
        
        print("Yj: ", Yj)   
        accuracy_sum = sum(Yj)
        
        print("Accuracy sum: ", accuracy_sum)


        accuracy = accuracy_sum / (N * L)

        numerator = (sum(Yj[i] * (L - Yj[i]) for i in range(N))) / L
        denominator = N * (L - 1) * accuracy * (1 - accuracy)

        

        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero")
        

        MIA = 1 - (numerator / denominator)

        return MIA