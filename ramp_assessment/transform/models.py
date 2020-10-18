from ..exception import InvalidInputArray
from ..util import to_float_array

import numpy as np
import pandas as pd

original_results_df = pd.DataFrame(
    {"Week 1": [1,1,1,1,1,1,1],"Week 2": [2,2,2,2,2,2,2],"Week 3": [3,3,3,3,3,3,3]}, 
    index=[1,2,3,4,5,6,7],
    dtype="float64", 
    copy=True
)

class InputData:

    def __init__(self, input_data):
        self.input_data = input_data
        self.validate()
        self._input_list = input_data["input"].split(",")

    def to_np_float_array(self):
        float_array = to_float_array(self._input_list)
        return np.array(float_array)

    def validate(self):
        example_input = '{"input": "0.1,0.9,0.123,0.99,0.5,1.0,0"}'

        if not self.input_data:
            raise InvalidInputArray("Invalid request body: Expected JSON object with string 'input' attribute. e.g. {}".format(example_input))
        
        if "input" not in self.input_data.keys():
            raise InvalidInputArray("Invalid request body: Missing 'input' attribute. e.g. {}".format(example_input))

        input_str = self.input_data["input"]
        if not isinstance(input_str, str):
            raise InvalidInputArray("Invalid request body: Expected 'input' attribute of type 'string'. e.g. {}".format(example_input))

        input_list = input_str.split(",")
        float_array = []
        try:
            float_array = to_float_array(input_list)
        except Exception:
            raise InvalidInputArray("Invalid request body: Provide 'input' attribute contains unexpected characters. The 'input' string should contain comma-separated decimal values only.")

        length = len(float_array)
        if length != 7:
            raise InvalidInputArray("Invalid request body: Provided 'input' array contains {} decimal values. Expected 7 comma-separated decimal values.".format(length))

    @property
    def input_list(self):
        return self._input_list