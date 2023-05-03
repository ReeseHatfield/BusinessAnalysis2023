import csv
class DataReader:
    
    def __init__ (self, file_path):
        self.file_path = file_path
        self.fields = []
        self.rows = []

        with open(file_path, 'r') as data:
            csv_reader = csv.reader(data)

            self.fields = next(csv_reader)

            # extracting each data row one by one
            for row in csv_reader:
                self.rows.append(row)

    def getAllData(self):
        return self.rows
    
    def getField(self, field_num):
        fields_at_index = []
        for i in range(len(self.rows)):
            fields_at_index.append(self.rows[i][field_num])
        return fields_at_index

    def getRow(self, row_num):
        return self.rows[row_num]



