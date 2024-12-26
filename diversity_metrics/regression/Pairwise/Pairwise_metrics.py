import numpy as np
from .Pairwise_base_metric import PairwiseRegressionMetric
from scipy.stats import rankdata




class CorrelationCoefficient_reg(PairwiseRegressionMetric):
    """
    Calculate the Pearson correlation coefficient between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the Pearson correlation coefficient between y1 and y2.

        Returns:
        float: Pearson correlation coefficient.
        """
        # Calculate covariance
        covariance = np.cov(self.y1, self.y2)[0, 1]
        
        # Calculate standard deviations
        std_y1 = np.std(self.y1)
        std_y2 = np.std(self.y2)
        

        denomenator = std_y1 * std_y2   
        if denomenator == 0:
            raise ZeroDivisionError("Denominator is zero")
        
        # Calculate correlation coefficient
        return covariance / denomenator
    

class MeanSquaredDifference(PairwiseRegressionMetric):
    """
    Calculate the mean squared difference between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the mean squared difference between y1 and y2.

        Returns:
        float: Mean squared difference.
        """
        
        return np.mean((self.y1 - self.y2) ** 2)
    

class MeanAbsoluteDifference(PairwiseRegressionMetric):
    """
    Calculate the mean absolute difference between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the mean absolute difference between y1 and y2.

        Returns:
        float: Mean absolute difference.
        """
        
        return np.mean(np.abs(self.y1 - self.y2))


class ErrorCorrelation(PairwiseRegressionMetric):
    """
    Calculate the error correlation between the outputs of two regressors.
    """
    
    def calculate(self):
        """
        Calculate the error correlation between y1 and y2.

        Returns:
        float: Error correlation.
        """
        
        return np.corrcoef(self.y1 - self.y_true, self.y2 - self.y_true)[0, 1]
    

class DisagreementMesure(PairwiseRegressionMetric):
    """
    Calculate the Disagreement Measure between two regressors.

    
    """
        
    def calculate(self):
        """
        Calculate the Disagreement Measure between y1 and y2.

        Returns:
        float: Disagreement Measure.
        """
        
        if self.threshold is None:
            raise ValueError("Threshold must be specified")
        disagreement_count = np.sum(np.abs(self.y1 - self.y2) > self.threshold)

        return disagreement_count / len(self.y1)


class RankCorrelation(PairwiseRegressionMetric):
    """
    Calculate the Rank Correlation between two regressors.
    """
        
    def calculate(self):
        """
        Calculate Spearman's rank correlation (ρ) between y1 and y2.

        Returns:
        float: Spearman's rank correlation coefficient.
        """

        # Calculate the rank of y1 and y2

        rank_y1 = rankdata(self.y1)
        rank_y2 = rankdata(self.y2)
        
        d= rank_y1 - rank_y2

        #Calculate the spearman's rank correlation


        sum_d_square = np.sum(d**2)
        spearmans= 1 - (6*sum_d_square)/(len(self.y1)*(len(self.y1)**2 -1))

        return spearmans
    

class Qstatistic_reg(PairwiseRegressionMetric):
    """
    Calculate the Q statistic between two regressors.
    """
        
    def calculate(self):
        """
        Calculate the Q statistic between y1 and y2.

        Returns:
        float: Q statistic.
        """

        if self.y_true is None:
            raise ValueError("The real observations are required for the Q statistic.")
        
        # Calculate the contingency table values as scalar counts
        a = np.sum((self.y1 == self.y_true) & (self.y2 == self.y_true))      # Both match y_true
        b = np.sum((self.y1 == self.y_true) & (self.y2 != self.y_true))      # y1 matches y_true, y2 does not
        c = np.sum((self.y1 != self.y_true) & (self.y2 == self.y_true))      # y2 matches y_true, y1 does not
        d = np.sum((self.y1 != self.y_true) & (self.y2 != self.y_true))      # Neither matches y_true

        

        denominator = ((a*d) + (c*d))
        

        if denominator == 0:
            raise ZeroDivisionError("Denominator ((a*d) + (c*d)) is zero")
        
        return (a*d - b*c) / denominator
    

class CovarianceError(PairwiseRegressionMetric):
    """
    Calculate the Covariance Error between two regressors.
    """
        
    def calculate(self):
        """
        Calculate the Covariance Error between y1 and y2.

        Returns:
        float: Covariance Error.
        """

        if self.y_true is None:
            raise ValueError("The real observations are required for the Covariance Error.")
        
        # Calculate the covariance of the errors
        
        mean_error_y1 = np.mean(self.y1 - self.y_true)
        mean_error_y2 = np.mean(self.y2 - self.y_true)

        error1= self.y1 - self.y_true
        error2= self.y2 - self.y_true

        covariance = np.mean((error1 - mean_error_y1) * (error2 - mean_error_y2))

        return covariance
    

class PartialCorrelationCoefficient(PairwiseRegressionMetric):
    """
    Calculate the Partial Correlation Coefficient between two regressors.
    """
        
    def calculate(self):
        """
        Calculate the Partial Correlation Coefficient between y1 and y2.

        Returns:
        float: Partial Correlation Coefficient.
        """
        if self.y_true is None:
            raise ValueError("The real observations are required for the Partial Correlation Coefficient.")

        # Calculate the pairwise correlations
        rho_y1_y2 = CorrelationCoefficient_reg(self.y1, self.y2).calculate()
        rho_y1_ytrue = CorrelationCoefficient_reg(self.y1, self.y_true).calculate()
        rho_y2_ytrue = CorrelationCoefficient_reg(self.y2, self.y_true).calculate()

        

        # Calculate partial correlation coefficient
        numerator = rho_y1_y2 - (rho_y1_ytrue * rho_y2_ytrue)
        denominator = np.sqrt((1 - rho_y1_ytrue**2) * (1 - rho_y2_ytrue**2))
        
        if denominator == 0:
            raise ValueError("Denominator is zero, partial correlation is undefined.")

        partial_correlation = numerator / denominator

        return partial_correlation


class DoubleFaultMeasure_reg(PairwiseRegressionMetric):
    """
    Calculate the Double Fault Measure between two regressors.
    """
        
    def calculate(self):
        """Counts instances where both regressors have large errors simultaneously
        
        Returns:
        float: Double Fault Measure.
        """
        if self.threshold is None:
            raise ValueError("Threshold must be specified for the Double Fault Measure.")
        if self.y_true is None:
            raise ValueError("The real observations are required for the Double Fault Measure.")
        
        count = np.sum((np.abs(self.y1 - self.y_true) > self.threshold) & (np.abs(self.y2 - self.y_true) > self.threshold))

        return count / len(self.y1)