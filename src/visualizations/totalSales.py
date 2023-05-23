from src.constants import summer_21_dates, summer_22_dates

import sys
import os
from src.parsing.DataReader import DataReader
import warnings
from dateutil.parser import parse
from dateutil import tz
from matplotlib import pyplot as plt
import numpy as np
from collections import OrderedDict


def main():
    print("Starting ", os.path.basename(__file__), "...")

    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))

    sales_per_day = get_sales_per_day(reader)

    compute_summer_deficit(list(sales_per_day.values()))

    user_input = input("Would you like to sort data by weeks or days? (w/d) ")
    is_by_weeks = True if user_input.lower() == "w" else False

    plot_data(sales_per_day, is_by_weeks)


def get_sales_per_day(reader: DataReader) -> OrderedDict:
    print("Reading sales per day...")
    sales_per_day = OrderedDict()
    num_sales_in_day = 0
    timezone_info = {'EDT': tz.gettz('America/New_York')}

    for i in range(2, reader.getNumRows()):

        previous_date = parse(reader.getRow(i - 1)[0], tzinfos=timezone_info)
        current_date = parse(reader.getRow(i)[0], tzinfos=timezone_info)

        if current_date.date() == previous_date.date():
            num_sales_in_day += 1
        else:
            sales_per_day[current_date] = num_sales_in_day
            num_sales_in_day = 0

    print("Finished reading sales per day")
    return sales_per_day


def plot_data(data: OrderedDict, is_by_weeks: bool) -> None:
    print("Plotting Data...")
    divider = 4 if is_by_weeks else 1

    days = np.arange(len(data))
    plt.bar(days / divider, list(data.values()), edgecolor=None)
    plt.xlabel("Day")
    plt.ylabel("Sales")
    print("Finished plotting data.")
    plt.show()


def compute_summer_deficit(sales: list) -> None:
    daily_average_sales = average_sales(sales)
    print("Average daily sales: ", round(daily_average_sales, 2))

    summer_avg = average_sales([
        compute_seasonal_avg(sales, summer_21_dates[0], summer_21_dates[1]),
        compute_seasonal_avg(sales, summer_22_dates[0], summer_22_dates[1])
    ])
    print("Summer Average: ", round(summer_avg, 2))

    busy_season_avg = average_sales([
        compute_seasonal_avg(sales, 0, summer_21_dates[0] - 1),
        compute_seasonal_avg(sales, summer_21_dates[1] + 1, summer_22_dates[0] - 1),
        compute_seasonal_avg(sales, summer_22_dates[1] + 1, len(sales))
    ])
    print("Busy season average: ", round(busy_season_avg, 2))

    summer_sales_deficit = summer_avg / busy_season_avg
    print(f"Summer sales deficit: -{round(100 * (1 - summer_sales_deficit), 2)}%")


def compute_seasonal_avg(sales: list, start: int, end: int) -> float:
    divisor: int = 0
    total: int = 0
    for i in range(len(sales)):
        if start <= i <= end:
            total += sales[i]
            divisor += 1
    avg: float = total / divisor

    return avg


def average_sales(sales: list) -> float:
    return sum(sales) / len(sales)


if __name__ == "__main__":
    main()
