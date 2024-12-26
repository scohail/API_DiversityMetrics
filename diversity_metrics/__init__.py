# diversity_metrics/__init__.py

# Import regression metrics
from .regression.Pairwise import Pairwise_metrics as reg_pairwise
from .regression.NonPairwise import Nonpairwise_metrics as reg_non_pairwise

# Import classification metrics (for later implementation)
from .classification.Pairwise import pairwise_metrics as cls_pairwise
from .classification.NonPairwise import Non_pairwise_metrics as cls_non_pairwise

# Provide access to all metrics under a single package-level namespace
__all__ = [
    'reg_pairwise', 'reg_non_pairwise',
    'cls_pairwise', 'cls_non_pairwise'
]
