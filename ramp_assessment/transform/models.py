from ..exception import InvalidInputArray

import numpy as np
import pandas as pd

original_results_df = pd.DataFrame(
    {"Week 1": [1,1,1,1,1,1,1],"Week 2": [2,2,2,2,2,2,2],"Week 3": [3,3,3,3,3,3,3]}, 
    index=[1,2,3,4,5,6,7],
    dtype="float64", 
    copy=True
)

class InputData:

    def __init__(self, input_str):
        self.validate(input_str)
        self._input_list = input_str.split(",")

    def to_np_float_array(self):
        float_array = list(map(float, self._input_list))
        return np.array(float_array)

    def validate(self, input_str):
        if not input_str:
            raise InvalidInputArray("'input' attribute cannot be an empty string")
        try:
            input_str.split(",")
        except ValueError:
            raise InvalidInputArray("Provided 'input' attribute is not a comma-separated decimal values string")

    @property
    def input_list(self):
        return self._input_list