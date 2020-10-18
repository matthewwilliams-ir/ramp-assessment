import numpy as np
import pandas as pd

original_results_df = pd.DataFrame(
    {"Week 1": [1,1,1,1,1,1,1],"Week 2": [2,2,2,2,2,2,2],"Week 3": [3,3,3,3,3,3,3]}, 
    index=[1,2,3,4,5,6,7],
    dtype="float64", 
    copy=True
)

class InputVector:

    def __init__(self, input_str):
        # TODO: Validate input
        self._input_list = input_str.split(",")

    def to_numpy_float_array(self):
        float_array = list(map(float, self._input_list))
        return np.array(float_array)

    @property
    def input_list(self):
        return self._input_list