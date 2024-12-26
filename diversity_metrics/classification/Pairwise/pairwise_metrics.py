from .Pairwise_base_metric import PairwiseClassificationMetric
import numpy as np






class CorrelationCoefficient(PairwiseClassificationMetric):
    """
    Correlation Coefficient (ρ) metric to measure the similarity between
    two classifiers based on their predictions and true labels.
    """

    def calculate(self):
        """
        Calculate the Correlation Coefficient (ρ) for two classifiers.

        Returns:
        float: The correlation coefficient (ρ) value between -1 and 1.

        Raises:
        ZeroDivisionError: If the denominator is zero.
        """
        # Get binary counts for A, B, C, D
        a, b, c, d = self._binary_counts()
        
        # Calculate the numerator and denominator for the correlation coefficient formula
        numerator = (a * d) - (b * c)
        denominator = np.sqrt((a + b) * (c + d) * (a + c) * (b + d))
        
        # Check for zero denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero")

        # Calculate correlation coefficient
        rho = numerator / denominator
        return rho
    


class QStatistics(PairwiseClassificationMetric):
    """
    Q Statistics metric to measure the level of agreement between two classifiers.
    """

    def calculate(self):
        """
        Calculate the Q Statistics for two classifiers.

        Returns:
        float: The Q Statistics value between -1 and 1.

        Raises:
        ZeroDivisionError: If the denominator is zero.
        """
        # Get binary counts for A, B, C, D
        a, b, c, d = self._binary_counts()

        print(a, b, c, d)

        
        # Calculate the numerator and denominator for the Q Statistics formula
        numerator = (a * d) - (b * c)
        denominator = (a * d) + (c * b)
        
        # Check for zero denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero")

        # Calculate Q Statistics
        q = numerator / denominator
        return q
    
class DifferencesMeasure(PairwiseClassificationMetric):
    """
    Differences Measure metric that captures the proportion of examples where the two classifiers disagree.
    """

    def calculate(self):
        """
        Calculate the Differences Measure for two classifiers.

        Returns:
        float: The Differences Measure value between -1 and 1.

        Raises:
        ZeroDivisionError: If the denominator is zero.
        """
        # Get binary counts for A, B, C, D
        a, b, c, d = self._binary_counts()
        
        # Calculate the numerator and denominator for the Differences Measure formula
        numerator = (b + c)
        denominator = (a + b + c + d)

        # Check for zero denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero") 

        # Calculate Differences Measure

        dm = numerator / denominator

        return dm
    

class DoubleFaultMeasure(PairwiseClassificationMetric):
    """
    Double Fault Measure metric that considers the failure of two classifiers simultaneously
    """
    def calculate(self):
        """
        Calculate the Double Fault Measure for two classifiers.

        Returns:
        float: The Double Fault Measure value between -1 and 1.

        Raises:
        ZeroDivisionError: If the denominator is zero.
        """
        # Get binary counts for A, B, C, D
        a, b, c, d = self._binary_counts()
        print(a, b, c, d)
        # Calculate the numerator and denominator for the Double Fault Measure formula
        numerator = d
        denominator = a + b + c + d

        # Check for zero denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero") 

        # Calculate Double Fault Measure

        dfm = numerator / denominator

        return dfm
    


class CombinationD_DF(PairwiseClassificationMetric):
    """
    This measure is a combination between the Differences Measure and the Double Fault Measure 
    """
    def calculate(self):
        """
        Calculate the Combination of Differences Measure and Double Fault Measure for two classifiers.

        Returns:
        float: The Combination of Differences Measure and Double Fault Measure value between -1 and 1.

        Raises:
        ZeroDivisionError: If the denominator is zero.
        """
      
        # Calculate the numerator and denominator for the Combination of Differences Measure and Double Fault Measure formula
        numerator = DifferencesMeasure.calculate(self) 
        print('numerator', numerator)
        denominator = DoubleFaultMeasure.calculate(self)
        print('denominator', denominator)
        # Check for zero denominator
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero") 

        # Calculate Combination of Differences Measure and Double Fault Measure

        cdfm = numerator / denominator

        return cdfm