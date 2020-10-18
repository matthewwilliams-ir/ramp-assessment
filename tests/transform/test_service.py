from ramp_assessment.transform.service import TransformService
import json
import pandas as pd

def test_multiply(service):
    input = {"input": "0.1,0.9,0.123,0.99,0.5,1.0,0"}
    df = pd.DataFrame(
        {"week_1": [1,1,1,1,1,1,1],"week_2": [2,2,2,2,2,2,2],"week_3": [3,3,3,3,3,3,3]}, 
        index=[1,2,3,4,5,6,7],
        dtype="float64", 
        copy=True
    )

    result_json = service.multiply(input, df)

    actual_json = json.loads(result_json)
    assert {"week_1", "week_2", "week_3"}.issubset(set(actual_json.keys()))
    assert {"1": 0.1,"2": 0.9,"3": 0.123,"4": 0.99,"5": 0.5,"6": 1.0,"7": 0.0} == actual_json["week_1"]
    assert {"1": 0.2,"2": 1.8,"3": 0.246,"4": 1.98,"5": 1.0,"6": 2.0,"7": 0.0} == actual_json["week_2"]
    assert {"1": 0.3,"2": 2.7,"3": 0.369,"4": 2.97,"5": 1.5,"6": 3.0,"7": 0.0} == actual_json["week_3"]

