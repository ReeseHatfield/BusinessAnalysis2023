import matplotlib.pyplot as plt
import sys
import os
import numpy as np


from src.parsing.DataReader import DataReader

from src.regression.PolynomialRegression import PolynomialRegression


def main():
    reader = DataReader(os.path.join('data', 'dataSet.csv'))

    sales = reader.get_sales_per_day()

    # animatePlot(sales)

    domain = range(len(sales))
    function = sales
    degree: int = 110

    model = np.poly1d(np.polyfit(domain, function, degree))
    line = np.linspace(1, len(sales), len(sales))
    plt.plot(domain, function)
    plt.plot(line, model(line), color="red")
    plt.show()


def animate_plot(sales):
    x = range(len(sales))
    y = sales

    for i in range(100):
        model = np.poly1d(np.polyfit(x, y, i))
        line = np.linspace(1, len(sales), len(sales))
        plt.plot(x, y)
        plt.plot(line, model(line), color="red")
        plt.savefig("degree_" + str(i) + ".png")

        plt.clf()


if __name__ == "__main__":
    main()
