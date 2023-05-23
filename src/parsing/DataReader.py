import csv
from dateutil import tz
import datetime as dt
import datetime
from dateutil.parser import parse


from collections import OrderedDict, defaultdict


class DataReader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.fields = []
        self.rows = []
        self.numRows = 0

        with open(file_path, 'r') as data:
            csv_reader = csv.reader(data)

            self.fields = next(csv_reader)

            # extracting each data row one by one
            for row in csv_reader:
                self.rows.append(row)
                self.numRows += 1

    def get_avg_sales_per_day_in_month(self, month: int) -> float:
        # Initialize variable to store total sales and number of days
        total_sales = 0
        total_days = 0
        # Fetch all sales per day and associated dates
        dates = self.getDates()
        sales = self.get_sales_per_day()
        # Iterate over each day
        for i in range(len(dates)):
            # If the month of the date matches the input month, increment total_sales and total_days
            if dates[i].month == month:
                total_sales += sales[i]
                total_days += 1
        # If no sales data was found for the specified month, return 0
        if total_days == 0:
            return 0
        # Otherwise, return the average sales per day
        else:
            return total_sales / total_days


    def getAllData(self):
        return self.rows

    def getField(self, field_num):
        fields_at_index = []
        for i in range(len(self.rows)):
            fields_at_index.append(self.rows[i][field_num])
        return fields_at_index

    def getRow(self, row_num):
        return self.rows[row_num]

    # O(1) getter for number of rows
    def getNumRows(self):
        return self.numRows

    def getAvgSalesPerDayInYear(self):
        dates = self.getDates()
        sales = self.get_sales_per_day()

        returnList = []

        current_date = dt.datetime(year=2023, month=1, day=1)
        for i in range(0, 365):
            dateSum = 0
            divisor = 0
            for j in range(len(dates)):
                if dates[j].day == current_date.day and dates[j].month == current_date.month:

                    if sales[j] != 0:
                        dateSum += sales[j]
                        divisor += 1

            if divisor == 0:
                returnList.append(0)
            else:
                returnList.append(dateSum / divisor)

            current_date += datetime.timedelta(days=1)

        current_date = dt.datetime(year=2023, month=1, day=1)
        for i in range(365):
            print(current_date, ": ", returnList[i])
            current_date += datetime.timedelta(days=1)

        print((returnList))
        return returnList

    def getDates(self):
        dates = self.getField(0)
        timezone_info = {'EDT': tz.gettz('America/New_York')}
        datelist = []
        for i in range(2, len(dates)):

            previousDate = parse(self.getRow(i - 1)[0], tzinfos=timezone_info)
            currentDate = parse(self.getRow(i)[0], tzinfos=timezone_info)

            if (previousDate.date() != currentDate.date()):
                datelist.append(parse(dates[i]))

        return datelist

    def get_sales_per_day(self) -> list:

        print("Reading sales per day...")
        sales_per_day = []
        num_sales_in_day = 0
        timezone_info = {'EDT': tz.gettz('America/New_York')}

        for i in range(2, self.getNumRows()):

            previousDate = parse(self.getRow(i - 1)[0], tzinfos=timezone_info)
            currentDate = parse(self.getRow(i)[0], tzinfos=timezone_info)

            if currentDate.date() == previousDate.date():
                num_sales_in_day += 1
            else:
                sales_per_day.append(num_sales_in_day)
                num_sales_in_day = 0

        print("Finished reading sales per day")
        return sales_per_day
