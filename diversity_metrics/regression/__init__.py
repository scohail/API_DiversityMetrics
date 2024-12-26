# diversity_metrics/regression/__init__.py

# Import all functions from pairwise and non-pairwise metric modules

from.Pairwise.Pairwise_metrics import *
"""
from .pairwise_metrics import (
    CorrelationCoefficient,
    mean_squared_difference,
    mean_absolute_difference,
    error_correlation,
    disagreement_measure,
    rank_correlation,
    mutual_information,
    kl_divergence,
    yules_q_statistic,
    covariance_error,
    partial_correlation,
    double_fault_measure
    
)
"""
from .NonPairwise.Nonpairwise_metrics import *

"""
from .non_pairwise_metrics import (

    variance_of_outputs,
    ensemble_variance,
    negative_correlation_learning,
    coefficient_of_variation,
    diversity_density,
    error_variance,
    ambiguity_decomposition
    
)
"""
# Expose all imported functions
__all__ = [
    'CorrelationCoefficient'

    """
    , 'mean_squared_difference', 'mean_absolute_difference',
    'error_correlation', 'disagreement_measure', 'rank_correlation', 'mutual_information',
    'kl_divergence', 'yules_q_statistic', 'covariance_error', 'partial_correlation',
    'double_fault_measure', 'variance_of_outputs', 'ensemble_variance',
    'negative_correlation_learning', 'coefficient_of_variation', 'diversity_density',
    'error_variance', 'ambiguity_decomposition'
    """
]
