import unittest
from diversity_metrics.classification.Pairwise.features_selection import *
from diversity_metrics.classification.Pairwise.pairwise_metrics import QStatistics
y= (    [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
              )

y_true = [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]

y1= [np.array(pred) for pred in y]

print('len(y1)' ,y1[1])

def tes_FS():
    fs = FeatureSelection(y, y_true, 0.9)

    valid_columns = fs.calculate('QStatistics')

    print("Valid columns:", valid_columns)  


tes_FS()