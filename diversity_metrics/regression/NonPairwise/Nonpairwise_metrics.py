import numpy as np
from .NonPairwise_base_metric import NonPairwiseRegressionMetric
from scipy.stats import gaussian_kde

class VarianceOutputs(NonPairwiseRegressionMetric):
    """
    Calculate the Variance of Outputs metric for an ensemble of regressors.
    """

    def calculate(self):
        """
        Calculate the Variance of Outputs metric.

        Returns:
        float: The average variance of outputs across all data points.
        """
        
        
        # Calculate the mean prediction for each data point across all regressors
        mean_predictions = np.mean(self.predictions, axis=0)
        
        
        # Calculate the variance for each data point
        variances = np.mean((self.predictions - mean_predictions) ** 2, axis=0)
        result_list = variances.tolist()
        
        # Return the average variance across all data points
        
        return result_list



class Ambiguity(NonPairwiseRegressionMetric):
    """
    Calculate the expected disagreement between base learners and the ensemble prediction.the Ambiguity metric for an ensemble of regressors.
    """

    def calculate(self):
        """
        Calculate the Ambiguity metric.

        Returns:
        float: The average ambiguity across all data points.
        """
        
        # Calculate the mean prediction for each data point across all regressors
        var = VarianceOutputs(self.predictions).calculate()

        ambiguity = np.mean(var)

        return ambiguity
    


class VariationCoefficient(NonPairwiseRegressionMetric):
    """
    Calculate The ratio of the standard deviation to the mean of the outputs for each data point, highlighting relative variability.
    """

    def calculate(self):
        """
        Calculate the Variation Coefficient metric.

        Returns:
        float: The average variation coefficient across all data points.
        """
        
        # Calculate the mean prediction for each data point across all regressors
        mean_predictions = np.mean(self.predictions, axis=0)
        
        # Calculate the standard deviation for each data point
        std = np.std(self.predictions, axis=0)
        
        variation_coefficient = (std/mean_predictions)
        CV = variation_coefficient.tolist()
        return CV
    

class DiversityDensity(NonPairwiseRegressionMetric):
    """
    Estimate the density of predictions in the output space and assess diversity inversely proportional to this density.
    (needs to figure out !!!!)
    """

    def calculate(self):
        """
        Calculate the Diversity Density metric using KDE.

        Returns:
        float: The average inverse density (diversity measure) across all data points.
        """
        # Stack predictions to shape (num_regressors, num_data_points)
        predictions = np.array(self.predictions)
        num_data_points = predictions.shape[1]

        # Calculate diversity density for each data point
        inverse_densities = []
        for k in range(num_data_points):
            # Extract predictions for the k-th data point across all regressors
            predictions_k = predictions[:, k].tolist()

            print(predictions_k)
            
            # Perform Kernel Density Estimation on predictions for the current data point
            kde = gaussian_kde(predictions_k)
            
            # Evaluate the KDE at each prediction point to get density estimates
            density_values = kde(predictions_k)

            print(density_values)
            
            # Calculate mean density and take its inverse for diversity
            mean_density = np.mean(density_values)
            inverse_density = 1.0 / mean_density if mean_density != 0 else np.inf
            inverse_densities.append(inverse_density)
        
        # Return the average inverse density across all data points
        return np.mean(inverse_densities)


class ErrorVariance(NonPairwiseRegressionMetric):
    """
    Calculate the Variance of the errors across all base regressors, reflecting diversity in model errors.
    """

    def calculate(self):
        """
        Calculate the Error Variance metric.

        Returns:
        float: The average error variance across all data points.
        """
        
        if self.y_true is None:
            raise ValueError("True values are required to calculate Error Variance.")
    
        # calculate the mean error for each data point across all regressors

        mean_errors = np.mean(self.predictions - self.y_true, axis=0)

        var = np.mean((self.predictions - self.y_true - mean_errors) ** 2, axis=0)

        return var.tolist()
    

class AmbiguityDecomposition(NonPairwiseRegressionMetric):
    """
    Variance of the errors across all base regressors, reflecting diversity in model errors.
    """
    def calculate(self):
        """
        Calculate the Ambiguity Decomposition metric.

        Returns:
        float: The average ambiguity decomposition across all data points.
        """
        
        if self.y_true is None:
            raise ValueError("True values are required to calculate Ambiguity Decomposition.")
        # Calculate the mean predictions 


        # Calclaute the error between the true values and the predictions

        error = np.mean(self.predictions - self.y_true)**2
        mean_predictions = np.mean(self.predictions, axis=0)
        # Calculate the variance for each data point
        Ambiguity = np.mean((self.predictions - mean_predictions) ** 2, axis=0)

        AD=  error - Ambiguity

        return AD.tolist()
    