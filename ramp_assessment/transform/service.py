from .models import InputData, original_results_df

class TransformService:
    
    def multiply(self, input_data, df):
        input_data = InputData(input_data)
        
        numpy_float_array = input_data.to_np_float_array()

        result_df = df.mul(numpy_float_array, axis=0)
        return result_df.to_json()

    def get_original_results_df(self):
        return original_results_df