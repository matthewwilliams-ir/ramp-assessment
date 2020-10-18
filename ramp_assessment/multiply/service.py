import numpy as np
import pandas as pd

def transform(input_str):

    # TODO: Validate input here
    # TODO: Map input to numpy float array
    input_list = input_str.split(",")
    input_float_array = list(map(float, input_list))
    np_array = np.array(input_float_array)

    # TODO: Create 3*7 DataFrame
    df = pd.DataFrame({"A": [1,1,1,1,1,1,1],"B": [2,2,2,2,2,2,2],"C": [3,3,3,3,3,3,3]}, index=[1,2,3,4,5,6,7], dtype="float64", copy=True)

    # TODO: Transform
    result_df = df.mul(np_array, axis=0) # Compare with .apply()

    return result_df.to_json()