from src.parsing.DataReader import DataReader
import os
import pickle
import datetime


def main():
    weather_pickle_path = os.path.join('dataset', 'weather_data_by_day.pkl')
    weather_data = None

    with open(weather_pickle_path, 'rb') as f:
        weather_data = pickle.load(f)
    date_to_retrieve = datetime.date(2020, 9, 1)
    data = weather_data[date_to_retrieve]

    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))
    for i in range(1,13):
        print(f"Average Sales in month {i}: {reader.get_avg_sales_per_day_in_month(i)}")


if __name__ == "__main__":
    main()
