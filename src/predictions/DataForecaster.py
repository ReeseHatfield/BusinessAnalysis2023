
class DataForecaster:
    def __init__(self, serialized_file_paths: tuple[str, str]):
        historical_discrete_model_path, poly_cont_model_path = serialized_file_paths

        self.historical_model = None

    # employee hours vs sales







