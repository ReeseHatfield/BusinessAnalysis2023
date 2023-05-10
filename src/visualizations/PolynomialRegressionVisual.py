import matplotlib.pyplot as plt
import sys
import os
import numpy as np
from numpy.polynomial import Polynomial as P

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'parsing')))
from DataReader import DataReader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'regression')))
from PolynomialRegression import PolynomialRegression

def main():
    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))
    sales = reader.getSalesPerDay()

    degree: int = 5
    x = range(len(sales))
    y = sales

    for i in range(100):

        model = np.poly1d(np.polyfit(x,y,i))
        line = np.linspace(1, len(sales), len(sales))
        plt.plot(x, y)
        plt.plot(line, model(line), color="red")
        plt.savefig("degree_" + str(i) + ".png")
       
        plt.clf()
       

if __name__ == "__main__":
    main()