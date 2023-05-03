from constants import apiKey, merchantID
import datetime as dt
from DataReader import DataReader


def main():
    reader = DataReader('dataset\dataSet.csv')
    print(reader.getField(0))
    


if(__name__ == "__main__"):
    main()