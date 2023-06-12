import os
import sys
import requests
import datetime
import pickle

from src.parsing.DataReader import DataReader

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"
LATITUDE = 39.344538
LONGITUDE = -82.988237


def gather_historical_data():

    print(os.getcwd())

    pickle_file_path = os.path.join('data', 'dates.pkl')

    if os.path.exists(pickle_file_path):
        print("Using pre-computed data")
        with open(pickle_file_path, 'rb') as f:
            dates = pickle.load(f)
    else:
        print("Computing data")
        reader = DataReader(os.path.join('data', 'dataSet.csv'))
        dates = reader.get_dates()
        with open(pickle_file_path, 'wb') as f:
            pickle.dump(dates, f)

    weather_dict_by_day = {}

    # Define date in ISO format
    for date in dates:
        current_date = date.date()

        # Define parameters for the API request
        request_params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "start_date": current_date,
            "end_date": current_date,
            "daily": "temperature_2m_mean,precipitation_sum",
            "timezone": "America/New_York",
            "temperature_unit": "fahrenheit",
            "precipitation_unit": "inch"
        }

        # Send GET request to Open-Meteo API
        response = requests.get(BASE_URL, params=request_params).json()

        mean_temperature = response['daily']['temperature_2m_mean'][0]
        precipitation_sum = response['daily']['precipitation_sum'][0]

        print(f"Day: {current_date}")
        print(mean_temperature)
        print(precipitation_sum)
        weather_dict_by_day[current_date] = (mean_temperature, precipitation_sum)

    weather_pickle_path = os.path.join('data', 'serialized', 'weather_data_by_day.pkl')
    with open(weather_pickle_path, 'wb') as f:
        pickle.dump(weather_dict_by_day, f)


if __name__ == "__main__":
    gather_historical_data()
