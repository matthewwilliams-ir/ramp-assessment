from .models import InputVector, original_results_df

class MultiplyService:
    
    def transform(self, input_str):
        input_vector = InputVector(input_str)
        numpy_float_array = input_vector.to_numpy_float_array()
        result_df = original_results_df.mul(numpy_float_array, axis=0) # Compare with .apply()
        return result_df.to_json()