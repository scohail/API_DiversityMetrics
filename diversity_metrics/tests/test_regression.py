import unittest
from diversity_metrics.regression.Pairwise.Pairwise_metrics import CorrelationCoefficient, Q_statistic

class TestCorrelationCoefficient(unittest.TestCase):

    def test_divisionbyzero(self):
        self.assertRaises(ValueError)