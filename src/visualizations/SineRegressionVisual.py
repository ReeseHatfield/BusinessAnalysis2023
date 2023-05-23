from src.parsing.DataReader import DataReader
from src.regression.SinusoidalRegression import SinusoidalRegression

import pylab as plt
import os


def main():
    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))
    sales = reader.get_sales_per_day()

    # tt = numpy.linspace(0, n, n)
    domain = range(len(sales))
    function = sales
    # result = fit_sin(domain, function)
    regression = SinusoidalRegression(domain, function)
    result = regression.fit_sin()

    plot_data(domain, function, result)


def plot_data(domain, function, result):
    plt.plot(domain, function, "-k", label="y", linewidth=2)
    plt.plot(domain, result["fitfunc"](domain), "r-", label="y fit curve", linewidth=2)
    plt.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    main()
