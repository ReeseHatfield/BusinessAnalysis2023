import csv
from dateutil import tz
import datetime as dt
import datetime
from dateutil.parser import parse


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
        dates = self.get_dates()
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

    def get_all_data(self):
        return self.rows

    def get_field(self, field_num):
        fields_at_index = []
        for i in range(len(self.rows)):
            fields_at_index.append(self.rows[i][field_num])
        return fields_at_index

    def get_row(self, row_num):
        return self.rows[row_num]

    # O(1) getter for number of rows
    def get_num_rows(self):
        return self.numRows

    def get_avg_sales_per_day_in_year(self):
        dates = self.get_dates()
        sales = self.get_sales_per_day()

        return_list = []

        current_date = dt.datetime(year=2023, month=1, day=1)
        for i in range(0, 365):
            date_sum = 0
            divisor = 0
            for j in range(len(dates)):
                if dates[j].day == current_date.day and dates[j].month == current_date.month:

                    if sales[j] != 0:
                        date_sum += sales[j]
                        divisor += 1

            if divisor == 0:
                return_list.append(0)
            else:
                return_list.append(date_sum / divisor)

            current_date += datetime.timedelta(days=1)

        current_date = dt.datetime(year=2023, month=1, day=1)
        for i in range(365):
            print(current_date, ": ", return_list[i])
            current_date += datetime.timedelta(days=1)

        print(return_list)
        return return_list

    def get_dates(self):
        dates = self.get_field(0)
        timezone_info = {'EDT': tz.gettz('America/New_York')}
        date_list = []
        for i in range(2, len(dates)):

            previous_date = parse(self.get_row(i - 1)[0], tzinfos=timezone_info)
            current_date = parse(self.get_row(i)[0], tzinfos=timezone_info)

            if previous_date.date() != current_date.date():
                date_list.append(parse(dates[i]).date())

        return date_list

    def get_sales_by_day(self) -> dict:
        sales_by_day = {}

        # Fetch all sales per day and associated dates
        dates = self.get_dates()
        sales = self.get_sales_per_day()

        # Iterate over each day
        for i in range(len(dates)):
            # If the date is already in the dictionary, add the sales to it
            if dates[i] in sales_by_day:
                sales_by_day[dates[i]] += sales[i]
            else:  # Otherwise, create a new entry in the dictionary for this date
                sales_by_day[dates[i]] = sales[i]

        return sales_by_day

    def get_sales_per_day(self) -> list:

        print("Reading sales per day...")
        sales_per_day = []
        num_sales_in_day = 0
        timezone_info = {'EDT': tz.gettz('America/New_York')}

        previous_date = parse(self.get_row(0)[0], tzinfos=timezone_info)

        for i in range(1, self.get_num_rows()):
            current_date = parse(self.get_row(i)[0], tzinfos=timezone_info)

            if current_date.date() == previous_date.date():
                num_sales_in_day += 1
            else:
                sales_per_day.append(num_sales_in_day)
                num_sales_in_day = 1  # Reset to 1 for the new day
            previous_date = current_date  # Save the current date for the next iteration

        # Account for the last day
        sales_per_day.append(num_sales_in_day)

        print("Finished reading sales per day")
        return sales_per_day
