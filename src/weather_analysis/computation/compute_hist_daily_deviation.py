import pickle
import os
from datetime import datetime
from src.parsing.DataReader import DataReader

PRECIPITATION_THRESHOLD = 0.0

def main():
    avg_sales_per_day_in_year = os.path.join('dataset', 'serialized', 'sales_data.pkl')
    sales_data = None

    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))

    with open(avg_sales_per_day_in_year, 'rb') as f:
        sales_data = pickle.load(f)

    # dataset/serialized/weather_data_by_day.pkl
    date_sales_dict_path = os.path.join('dataset', 'serialized', 'weather_data_by_day.pkl')

    sales_by_date = reader.get_sales_by_day()

    weather_data = load_weather_dict_from_pickle(date_sales_dict_path)
    for date in weather_data:
        day_of_year = date.timetuple().tm_yday

        if weather_data[date][1] > PRECIPITATION_THRESHOLD:
            print(f"PRECIP on {date}")
            print(f"Normal: {sales_data[day_of_year]}")
            print(f"Today: {sales_by_date[date]}")

            divisor = sales_data[day_of_year] if sales_data[day_of_year] != 0 else 1

            print(f"PERCENT: {sales_by_date[date] / divisor}")

    for i in range(len(sales_data)):
        print(f"Normal Sales on day {i}: {sales_data[i]}")




    # day_of_year = datetime.now().timetuple().tm_yday


def load_weather_dict_from_pickle(weather_pickle_path: str):
    weather_data = None

    if not os.path.exists(weather_pickle_path):
        print(f"File does not exist: {weather_pickle_path}")
        raise FileNotFoundError

    try:
        with open(weather_pickle_path, 'rb') as f:
            weather_data = pickle.load(f)
    except (pickle.UnpicklingError, EOFError) as e:
        print(f"Error while reading the pickle file: {str(e)}")
        weather_data = None

    return weather_data


if __name__ == "__main__":
    main()
