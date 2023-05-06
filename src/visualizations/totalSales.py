import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'parsing')))
from DataReader import DataReader
import warnings
from dateutil.parser import parse, UnknownTimezoneWarning
from dateutil import tz
from datetime import datetime, timezone, timedelta
from matplotlib import pyplot as plt
import numpy as np
from collections import OrderedDict
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from constants import summer_21_dates, summer_22_dates


warnings.filterwarnings("ignore", category = UnknownTimezoneWarning)

def main():
    print("Starting ", os.path.basename(__file__),"...")

    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))

    sales_per_day = getSalesPerDay(reader)

    computeSummerDeficit(list(sales_per_day.values()))

    userInput = input("Would you like to sort data by weeks or days? (w/d) ")
    is_by_weeks = True if userInput.lower() == "w" else False
    

    plotData(sales_per_day, is_by_weeks)


    
    
def getSalesPerDay(reader: DataReader) -> OrderedDict:

    print("Reading sales per day...")
    sales_per_day = OrderedDict()
    num_sales_in_day = 0
    timezone_info = {'EDT': tz.gettz('America/New_York')}


    for i in range(2, reader.getNumRows()):

        previousDate = parse(reader.getRow(i-1)[0], tzinfos = timezone_info )
        currentDate = parse(reader.getRow(i)[0], tzinfos = timezone_info)

        if currentDate.date() == previousDate.date():
            num_sales_in_day += 1
        else:
            sales_per_day[currentDate] = num_sales_in_day
            num_sales_in_day = 0   

    print("Finished reading sales per day")
    return sales_per_day

def plotData(data: OrderedDict, is_by_weeks: bool) -> None:

    print("Plotting Data...")
    divider = 4 if is_by_weeks else 1

    days = np.arange(len(data))
    plt.bar(days / divider, list(data.values()), edgecolor = None)
    plt.xlabel("Day")
    plt.ylabel("Sales")
    print("Finished plotting data.")
    plt.show()
    
def computeSummerDeficit(sales: list) -> None:
    summer_21_start = summer_21_dates[0]
    summer_21_end = summer_21_dates[1]

    summer_22_start = summer_22_dates[0]
    summer_22_end = summer_22_dates[1]

    summer_21_avg = computeSeasonalAvg(sales, summer_21_start, summer_21_end)
    summer_22_avg = computeSeasonalAvg(sales, summer_22_start, summer_22_end)

    summer_avg = (summer_21_avg + summer_22_avg) / 2
    print("Summer Average: ", round(summer_avg, 2))

    busy_season_1 = computeSeasonalAvg(sales, 0, summer_21_start - 1)
    busy_season_2 = computeSeasonalAvg(sales, summer_21_end + 1, summer_22_start - 1)
    busy_season_3 = computeSeasonalAvg(sales, summer_22_end + 1, len(sales))

    busy_season_avg = (busy_season_1 + busy_season_2 + busy_season_3) / 3
    print("Busy season average: ", busy_season_avg)

    daily_average_sales = sum(sales) / len(sales)
    print("Average daily sales: ", round(daily_average_sales, 2))


def computeSeasonalAvg(sales: list, start: int, end: int) -> float:
    divisor: int = 0
    sum: int = 0
    for i in range(len(sales)):
        if(i >= start and i <= end):
            sum += sales[i]
            divisor += 1
    avg: float = sum / divisor

    return avg

def averageSales(sales: list) -> float:
    return sum(sales) / len(sales)


if __name__ == "__main__":
    main()