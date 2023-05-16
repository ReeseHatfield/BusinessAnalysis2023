import pickle
import matplotlib.pyplot as plt
import numpy as np

def main():
    sales = []
    model = []
    data_file = "dataset\sales_data.pkl"
    model_file = "dataset\model.pkl"
    with open(data_file, 'rb') as f:
        sales = pickle.load(f)
    with open(model_file, 'rb') as f:
        model = pickle.load(f)


    domain = range(len(sales))    
    plotData(domain, sales, model)
    
    
    
    
def plotData(domain, function, model):
    line = np.linspace(1, len(domain), len(domain))
    plt.plot(domain, function)
    plt.plot(line, model(line), color="red")
    plt.show()




if __name__ == "__main__":
    main()