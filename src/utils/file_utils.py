import os

from src.weather_analysis.computation.compute_monthly_deviation import compute_monthly_deviation
from src.weather_analysis.computation.compute_hist_daily_deviation import compute_hist_daily_deviation
from src.weather_analysis.historical.gather_historical_data import gather_historical_data


def check_files():
    crit_data_path = os.path.join('dataset', 'dataSet.csv')

    if not os.path.exists(crit_data_path):
        print("Error: critical dataset missing")
        print("Exiting...")
        exit(1)

    paths = [
        os.path.join('dataset', 'serialized', 'avg_sales_per_month.pkl'),
        os.path.join('dataset', 'serialized', 'model.pkl'),
        os.path.join('dataset', 'serialized', 'sales_data.pkl'),
        os.path.join('dataset', 'serialized', 'weather_data_by_day.pkl'),
    ]

    all_exist = all(os.path.exists(path) for path in paths)

    if all_exist:
        print("All necessary files exist.")
    else:
        print("One or more paths do not exist. Computing necessary data")
        print("This may take a while...")
        gather_historical_data()
        compute_hist_daily_deviation()
        compute_monthly_deviation()
