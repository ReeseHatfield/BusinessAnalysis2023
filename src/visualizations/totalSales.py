import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'parsing')))
from DataReader import DataReader
from dateutil.parser import parse
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np
from collections import OrderedDict


def main():
    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))

    sales_per_day = getSalesPerDay(reader)
    is_by_weeks = False
    plotData(sales_per_day, is_by_weeks)

    
    print(len(sales_per_day))

    
    
def getSalesPerDay(reader: DataReader) -> OrderedDict:

    sales_per_day = OrderedDict()
    num_sales_in_day = 0

    for i in range(2, reader.getNumRows()):
        
        previousDate = parse(reader.getRow(i-1)[0])
        currentDate = parse(reader.getRow(i)[0])

        if currentDate.date() == previousDate.date():
            num_sales_in_day += 1
        else:

            if(currentDate.month == 6 or currentDate.month == 7 or currentDate.month == 8):
                num_sales_in_day += 000
    
            sales_per_day[currentDate] = num_sales_in_day
            
            num_sales_in_day = 0   

    return sales_per_day

def plotData(data: OrderedDict, is_by_weeks: bool) -> None:

    divider = 4 if is_by_weeks else 1

    days = np.arange(len(data))
    plt.bar(days / divider, list(data.values()), edgecolor = None)
    plt.xlabel("Day")
    plt.ylabel("Sales")
    plt.show()


if __name__ == "__main__":
    main()