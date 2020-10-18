from ramp_assessment.multiply.models import InputVector

def test_input_vector():
    input_str = "0.1,0.9,0.123,0.99,0.5,1.0,0"

    input_vector = InputVector(input_str)

    assert len(input_vector.input_list) == 7
    assert input_vector.input_list == ['0.1','0.9','0.123','0.99','0.5','1.0','0']

def test_input_vector_to_numpy_float_array():
    input_str = "0.1,0.9,0.123,0.99,0.5,1.0,0"

    input_vector = InputVector(input_str)
    np_float_array = input_vector.to_numpy_float_array()

    assert len(np_float_array) == 7
    assert np_float_array.dtype == "float64"