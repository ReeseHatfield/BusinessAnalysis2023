import matplotlib.pyplot as plt
import sys
import pickle
import os
import numpy as np
from numpy.polynomial import Polynomial as P
from dateutil.parser import parse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..' ,'..', '..', 'src', 'parsing')))
from DataReader import DataReader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..', '..', '..', 'src', 'regression')))
from PolynomialRegression import PolynomialRegression

def main():
    # Load data from file if it exists, otherwise compute it
    sales, model = load_or_compute_data()

    # Plot the data
    plotData(range(len(sales)), sales, model)

def load_or_compute_data():
    data_file = "dataset\sales_data.pkl"
    model_file = "dataset\model.pkl"

    if os.path.exists(data_file) and os.path.exists(model_file):
        print("Using pre-computed data")
        # Load data from file
        with open(data_file, 'rb') as f:
            sales = pickle.load(f)
        with open(model_file, 'rb') as f:
            model = pickle.load(f)
    else:
        print("Computing data")
        # Compute data
        reader = DataReader(os.path.join('dataset', 'dataSet.csv'))
        sales = reader.getAvgSalesPerDayInYear()
        degree: int = 40
        domain = range(len(sales))
        model = np.poly1d(np.polyfit(domain, sales, degree))

        # Save data to file
        with open(data_file, 'wb') as f:
            pickle.dump(sales, f)
        with open(model_file, 'wb') as f:
            pickle.dump(model, f)

    return sales, model


    
    
def plotData(domain, function, model):
    line = np.linspace(1, len(domain), len(domain))
    plt.plot(domain, function)
    plt.plot(line, model(line), color="red")
    plt.show()


if __name__ == '__main__':
    main()