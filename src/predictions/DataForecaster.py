import pickle
from datetime import datetime
from src.constants import precip_dict


class DataForecaster:
    def __init__(self, serialized_file_paths: tuple[str, str]):
        historical_discrete_model_path, poly_cont_model_path = serialized_file_paths

        self._historical_model = None
        self._cont_model = None

        with open(historical_discrete_model_path, 'rb') as hist_file:
            self._historical_model = pickle.load(hist_file)

        with open(poly_cont_model_path, 'rb') as poly_file:
            self._cont_model = pickle.load(poly_file)

    def forecast(self, month, day, precip):
        date_str = f'{month}-{day}-2022'
        date_to_get = self._date_to_day(date_str)

        hist_forecast = self._historical_model[date_to_get]
        predicted_forecast = self._cont_model(date_to_get)

        print("here ", precip_dict[precip])



        hist_forecast -= hist_forecast * precip_dict[precip]
        predicted_forecast -= predicted_forecast * precip_dict[precip]


        return hist_forecast, predicted_forecast

    def _date_to_day(self, date_input: str):
        year = 2022
        date = datetime.strptime(date_input, f'%m-%d-%Y').date()
        day_of_year = date.timetuple().tm_yday
        return day_of_year

    # employee hours vs sales

    def get_historical_model(self):
        return self._historical_model

    def get_cont_model(self):
        return self._cont_model
