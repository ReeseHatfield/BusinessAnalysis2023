import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'parsing')))
from DataReader import DataReader
from dateutil.parser import parse


def main():
    exDate = "04-May-2023 09:28 AM EDT"
    parsedDate = parse(exDate)

    rowsNum = 80000#ish fix this, do not have access to proper data set


    print(parsedDate.day)
    print(parsedDate.month)
    print(parsedDate.year)
    


if __name__ == "__main__":
    main()