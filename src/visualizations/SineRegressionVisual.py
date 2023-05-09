import numpy, scipy.optimize
import pylab as plt
import sys
import os
from dateutil import tz
from dateutil.parser import parse, UnknownTimezoneWarning
import warnings
warnings.filterwarnings("ignore", category = UnknownTimezoneWarning)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'parsing')))
from DataReader import DataReader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'regression')))
from SinusoidalRegression import SinusoidalRegression

def main():
    reader = DataReader(os.path.join('dataset', 'dataSet.csv'))
    sales = reader.getSalesPerDay()

    #tt = numpy.linspace(0, n, n)
    domain = range(len(sales))
    function = sales
    #result = fit_sin(domain, function)
    regression = SinusoidalRegression(domain, function)
    result = regression.fit_sin()

    print("Regression Coeffiecients: ", result)

    plt.plot(domain, function, "-k", label="y", linewidth=2)
    plt.plot(domain, result["fitfunc"](domain), "r-", label="y fit curve", linewidth=2)
    plt.legend(loc="best")
    plt.show()

if __name__ == "__main__":
    main()