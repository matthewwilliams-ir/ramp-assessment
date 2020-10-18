from ramp_assessment.transform.models import InputData
from ramp_assessment.exception import InvalidInputArray
import pytest

def test_input_data():
    input_data = InputData({"input": "0.1,0.9,0.123,0.99,0.5,1.0,0"})

    assert len(input_data.input_list) == 7
    assert input_data.input_list == ['0.1','0.9','0.123','0.99','0.5','1.0','0']

def test_input_data_validate_empty_json():
    with pytest.raises(InvalidInputArray):
        input_data = InputData({})
        input_data.validate()

def test_input_data_validate_missing_attr():
    with pytest.raises(InvalidInputArray):
        input_data = InputData({"other": ""})
        input_data.validate()

def test_input_data_validate_not_str():
    with pytest.raises(InvalidInputArray):
        input_data = InputData({"input": 5})
        input_data.validate()

def test_input_data_validate_unexpected_chars():
    with pytest.raises(InvalidInputArray):
        input_data = InputData({"input": "5.a,abc"})
        input_data.validate()

def test_input_data_validate_length():
    with pytest.raises(InvalidInputArray):
        input_data = InputData({"input": "5.0,6.1,3.0"})
        input_data.validate()

def test_input_data_to_numpy_float_array():
    input_data = InputData({"input": "0.1,0.9,0.123,0.99,0.5,1.0,0"})

    np_float_array = input_data.to_np_float_array()

    assert len(np_float_array) == 7
    assert np_float_array.dtype == "float64"