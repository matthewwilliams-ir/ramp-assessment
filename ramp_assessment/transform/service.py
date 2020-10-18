from .models import InputData, original_results_df

class TransformService:
    
    def multiply(self, input_str):
        input_data = InputData(input_str)
        numpy_float_array = input_data.to_np_float_array()
        
        result_df = original_results_df.mul(numpy_float_array, axis=0) # Compare with .apply()
        return result_df.to_json()