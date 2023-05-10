import matplotlib.pyplot as plt
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'parsing')))
from DataReader import DataReader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'regression')))
from LinearRegression import LinearRegression
def main():
    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))
    sales = reader.getSalesPerDay()

    x = np.arange(len(sales)).reshape(-1, 1)
    y = sales

    model = LinearRegression()
    model.fit(x, y)

    y_pred = model.predict(x)
    print("B0:", model.get_coeffs()[0])
    print("B1:", model.get_coeffs()[1])
    #y = b0 + b1*x

    plt.plot(x, y_pred, color='red')
    plt.scatter(x, y, color='blue')
    plt.xlim(0, 700)
    plt.ylim(0, 250)
    plt.show()

if __name__ == "__main__":
    main()


