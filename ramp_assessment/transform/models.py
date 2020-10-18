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
        if not self.input_data:
            raise InvalidInputArray("Expected json object with 'input' attribute")
        
        if "input" not in self.input_data.keys():
            raise InvalidInputArray("Missing 'input' attribute in provided request body")

        input_str = self.input_data["input"]
        if not isinstance(input_str, str):
            raise InvalidInputArray("Expected 'input' attribute of type 'string'")

        try:
            input_list = input_str.split(",")
            float_array = to_float_array(input_list)
            if len(float_array) != 7:
                raise InvalidInputArray("Provided 'input' array contains {} decimal values. Only 7 comma-separated  decimal values should be provided.".format(len(float_array)))
        except Exception:
            raise InvalidInputArray("Provide 'input' attribute contains unexpected characters. The 'input' string should contain comma-separated decimal values only.")

    @property
    def input_list(self):
        return self._input_list