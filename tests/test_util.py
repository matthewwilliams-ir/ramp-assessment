from ramp_assessment.util import to_float_array

def test_to_float_array():
    str_array = ['0.1', '0.2', '0.3', '0.4', '0.5']
    float_array = to_float_array(str_array)
    assert len(float_array) == 5
    assert float_array == [0.1, 0.2, 0.3, 0.4, 0.5]