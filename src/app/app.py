import pickle
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk

def main():

    root = tk.Tk()

    root.geometry("900x500")
    root.title("Sales")

    style = ttk.Style(root)
    style.configure('lefttab.TNotebook', tabposition='ws')
    tabControl = ttk.Notebook(root, style='lefttab.TNotebook')

    


    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Tab 1')
    tabControl.add(tab2, text='Tab 2')

    tabControl.pack(expand=1, fill="both")


    root.mainloop()
    
    

    historical_sales_avg, projected_avg_sales = readData("dataset\sales_data.pkl", "dataset\model.pkl")
    date_to_get = int(input("Date: "))

    print("Historical: ", round(historical_sales_avg[date_to_get], 2))

    print("Predicted: ", round(projected_avg_sales(date_to_get), 2))

    domain = range(len(historical_sales_avg))    
    plotData(domain, historical_sales_avg, projected_avg_sales)



def readData(data_file, model_file):
    sales = []
    model = []

    with open(data_file, 'rb') as f:
        sales = pickle.load(f)
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    return sales, model
    
    
    
    
def plotData(domain, function, model):
    line = np.linspace(1, len(domain), len(domain))
    plt.plot(domain, function)
    plt.plot(line, model(line), color="red")
    plt.show()




if __name__ == "__main__":
    main()