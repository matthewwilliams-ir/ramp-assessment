from ramp_assessment.multiply.service import MultiplyService

import json

def test_transform(service):
    input_str = "0.1,0.9,0.123,0.99,0.5,1.0,0"

    result_json = service.transform(input_str)

    actual_json = json.loads(result_json)
    assert {"Week 1", "Week 2", "Week 3"}.issubset(set(actual_json.keys()))
    assert {"1": 0.1,"2": 0.9,"3": 0.123,"4": 0.99,"5": 0.5,"6": 1.0,"7": 0.0} == actual_json["Week 1"]
    assert {"1": 0.2,"2": 1.8,"3": 0.246,"4": 1.98,"5": 1.0,"6": 2.0,"7": 0.0} == actual_json["Week 2"]
    assert {"1": 0.3,"2": 2.7,"3": 0.369,"4": 2.97,"5": 1.5,"6": 3.0,"7": 0.0} == actual_json["Week 3"]

