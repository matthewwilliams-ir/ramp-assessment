from ramp_assessment.transform.models import InputData

def test_input_vector():
    input_str = "0.1,0.9,0.123,0.99,0.5,1.0,0"

    input_data = InputData(input_str)

    assert len(input_data.input_list) == 7
    assert input_data.input_list == ['0.1','0.9','0.123','0.99','0.5','1.0','0']

def test_input_vector_to_numpy_float_array():
    input_str = "0.1,0.9,0.123,0.99,0.5,1.0,0"

    input_data = InputData(input_str)
    np_float_array = input_data.to_np_float_array()

    assert len(np_float_array) == 7
    assert np_float_array.dtype == "float64"