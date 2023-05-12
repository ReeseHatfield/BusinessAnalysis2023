import csv
import warnings
from dateutil import tz
from dateutil.parser import parse, UnknownTimezoneWarning
warnings.filterwarnings("ignore", category = UnknownTimezoneWarning)

class DataReader:
    
    def __init__ (self, file_path):
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
        sales = self.getSalesPerDay()

        dateSaleDict = {}
        for i in range(len(dates)):
            
            dateSaleDict[dates[i]] = sales[i]

        #TODO: make this average all sales made on same day of year, and return list of sales

    def getDates(self):
        dates = self.getField(0)
        timezone_info = {'EDT': tz.gettz('America/New_York')}
        datelist = []
        for i in range(2, len(dates)):

            previousDate = parse(self.getRow(i-1)[0], tzinfos = timezone_info )
            currentDate = parse(self.getRow(i)[0], tzinfos = timezone_info)

            if(previousDate.date() != currentDate.date()):
                 datelist.append(parse(dates[i]))
        
        return datelist
        
    
    def getSalesPerDay(self) -> list:

        print("Reading sales per day...")
        sales_per_day = []
        num_sales_in_day = 0
        timezone_info = {'EDT': tz.gettz('America/New_York')}

        for i in range(2, self.getNumRows()):

            previousDate = parse(self.getRow(i-1)[0], tzinfos = timezone_info )
            currentDate = parse(self.getRow(i)[0], tzinfos = timezone_info)

            if currentDate.date() == previousDate.date():
                num_sales_in_day += 1
            else:
                sales_per_day.append(num_sales_in_day)
                num_sales_in_day = 0   

        print("Finished reading sales per day")
        return sales_per_day



