import sys
import json
import numpy as np
from typing import List
import pandas as pd

from classification.Pairwise.pairwise_metrics import *
from classification.NonPairwise.Non_pairwise_metrics import *
from regression.Pairwise.Pairwise_metrics import *
from regression.NonPairwise.Nonpairwise_metrics import *

def process_file(data):

    cols: List[str] = data['data'][0]
    selected_cols: List[str] = data['columns']
    metrics: List[str] = data['metrics']


    print(metrics)
    print(cols)
    print(selected_cols)

    y= data['data']
    y_transposed = list(map(list, zip(*y)))
    y_transposed = [col[1:] for col in y_transposed]
    

    y1 = []
    y2 = []
    yt = []
    results = {}

    print('y values are',y_transposed)

    try:
        # Perform operations on the received JSON content
        for i in range(1, len(data['data'])):
            y1.append(data['data'][i][cols.index(selected_cols[0] if len(selected_cols) else cols[0])])
            y2.append(data['data'][i][cols.index(selected_cols[1] if len(selected_cols) > 1 else cols[1])])
            yt.append(data['data'][i][-1])

        print("y1 values are",y1)
        print("yt values are",yt)
        print("processing the metrics ")

        for i in range(len(data['metrics'])):
            print(data['metrics'])
            if data['metrics'][i] == "CorrelationCoefficient_clas":
                result = CorrelationCoefficient(y1, y2, yt).calculate()
                results['Correlation Coefficient_clas'] = result
            elif data['metrics'][i] == "QStatistics_clas":
                result = QStatistics(y1, y2, yt).calculate()
                results['QStatistics_clas'] = result
            elif data['metrics'][i] == "DifferencesMeasure":
                result = DifferencesMeasure(y1, y2, yt).calculate()
                results['DifferencesMeasure'] = result
            elif data['metrics'][i] == "DoubleFaultMeasure":
                result = DoubleFaultMeasure(y1, y2, yt).calculate()
                results['DoubleFaultMeasure'] = result
            elif data['metrics'][i] == "CombinationD_DF":
                result = CombinationD_DF(y1, y2, yt).calculate()
                results['CombinationD_DF'] = result



            elif data['metrics'][i] == "Entropy":
                result = Entropy(y_transposed, yt).calculate()
                results['Entropy'] = result
            elif data['metrics'][i] == "KohaviWolpertVariance":
                result = KohaviWolpertVariance(y_transposed, yt).calculate()
                results['KohaviWolpertVariance'] = result
            elif data['metrics'][i] == "MeasurementInterraterAgreement":
                result = MeasurementInterraterAgreement(y_transposed, yt).calculate()
                results['MeasurementInterraterAgreement'] = result






            elif data['metrics'][i] == "CorrelationCoefficient_reg":
                result = CorrelationCoefficient_reg(y1, y2, yt, threshold= 0.5).calculate()
                results['Correlation Coefficient_reg'] = result
            elif data['metrics'][i] == "MeanSquaredDifference":
                result = MeanSquaredDifference(y1, y2, yt, threshold= 0.5).calculate()
                results['MeanSquaredDifference'] = result
            elif data['metrics'][i] == "MeanAbsoluteDifference":
                result = MeanAbsoluteDifference(y1, y2, yt, threshold= 0.5).calculate()
                results['MeanAbsoluteDifference'] = result
            elif data['metrics'][i] == "ErrorCorrelation":
                result = ErrorCorrelation(y1, y2, yt, threshold= 0.5).calculate()
                results['ErrorCorrelation'] = result
            elif data['metrics'][i] == "DisagreementMesure":
                result = DisagreementMesure(y1, y2, yt, threshold= 0.5).calculate()
                results['DisagreementMesure'] = result
            elif data['metrics'][i] == "RankCorrelation":
                result = RankCorrelation(y1, y2, yt, threshold= 0.5).calculate()
                results['RankCorrelation'] = result
            elif data['metrics'][i] == "Qstatistic_reg":
                result = Qstatistic_reg(y1, y2, yt, threshold= 0.5).calculate()
                results['Qstatistic_reg'] = result
            elif data['metrics'][i] == "CovarianceError":
                result = CovarianceError(y1, y2, yt,threshold= 0.5).calculate()
                results['CovarianceError'] = result
            elif data['metrics'][i] == "PartialCorrelationCoefficient":
                result = PartialCorrelationCoefficient(y1, y2, yt,threshold= 0.5).calculate()
                results['PartialCorrelationCoefficient'] = result
            elif data['metrics'][i] == "DoubleFaultMeasure_reg":
                result = DoubleFaultMeasure_reg(y1, y2, yt,threshold= 0.5).calculate()
                results['DoubleFaultMeasure_reg'] = result


                        
            elif data['metrics'][i] == "VarianceOutputs":
                result = VarianceOutputs(y_transposed, yt).calculate()
                results['VarianceOutputs'] = result
            elif data['metrics'][i] == "Ambiguity":
                result = Ambiguity(y_transposed, yt).calculate()
                results['Ambiguity'] = result
            elif data['metrics'][i] == "VariationCoefficient":
                result = VariationCoefficient(y_transposed, yt).calculate()
                results['VariationCoefficient'] = result
            elif data['metrics'][i] == "DiversityDensity":
                result = DiversityDensity(y_transposed, yt).calculate()
                results['DiversityDensity'] = result
            elif data['metrics'][i] == "ErrorVariance":
                result = ErrorVariance(y_transposed, yt).calculate()
                results['ErrorVariance'] = result
            elif data['metrics'][i] == "AmbiguityDecomposition":
                result = AmbiguityDecomposition(y_transposed, yt).calculate()
                results['AmbiguityDecomposition'] = result
            
            

            
            else:
                results['error'] = "Invalid metric"
                return {"status": "error", "message": "Invalid metric"}


        # Example of processing: Modify or analyze the data, 
        # For instance, returning the length of the content as an example
        return {"status": "success", "data": results}
        
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    
    input_data = sys.argv[1]
    try:
        # Parse the received input data as JSON
        print("Received data: ", end="")
        print(input_data)
        print(type(input_data))

        data = json.loads(input_data)



        print("Parsed data: ", end="")
        print(data)
        print(type(data))
        # Process the parsed JSON data
        result = process_file(data)
        
        # Output the result as JSON
        print(json.dumps(result))
    
    except json.JSONDecodeError as e:
        print(json.dumps({"status": "error", "message": "Invalid JSON data", "details": str(e)}))
        sys.exit(1)
    except Exception as ee:
        print(json.dumps({"status": "error", "message": "Unknown error", "details": str(ee)}))
        sys.exit(1)