from constants import apiKey, merchantID
import datetime as dt
from parsing.DataReader import DataReader
import os


def main():
    reader = DataReader(os.path.join('dataset','dataSet.csv'))
    print(reader.getField(0))
    


if(__name__ == "__main__"):
    main()