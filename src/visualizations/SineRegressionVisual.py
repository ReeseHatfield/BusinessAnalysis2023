import os
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

from src.parsing.DataReader import DataReader
from src.regression.SinusoidalRegression import SinusoidalRegression


def compute_sine_visual():
    reader = DataReader(os.path.join('data', 'dataSet.csv'))
    sales = reader.get_sales_per_day()

    domain = range(len(sales))
    function = sales
    regression = SinusoidalRegression(domain, function)
    result = regression.fit_sin()

    plot_data(domain, function, result)


def plot_data(domain, function, result):
    plt.plot(domain, function, "-k", label="y", linewidth=2)
    plt.plot(domain, result["fitfunc"](domain), "r-", label="y fit curve", linewidth=2)
    plt.legend(loc="best")
    plt.show(block=False)


if __name__ == "__main__":
    compute_sine_visual()
