import pickle
import os
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from src.constants import weather_effect
from src.app.windows.MainWindow import MainWindow


def main():
    root = tk.Tk()

    customized_style = ttk.Style()
    customized_style.configure('Custom.TNotebook.Tab', padding=[12, 12], font=('Helvetica', 10))
    customized_style.configure('Custom.TNotebook', tabposition='wn')

    app = MainWindow(root)
    root.mainloop()



    sales_data_path = os.path.join('dataset', 'serialized', 'sales_data.pkl')
    cont_model = os.path.join('dataset', 'serialized', 'model.pkl')
    historical_sales_avg, projected_avg_sales = read_data(sales_data_path, cont_model)

    date_to_get = date_to_day((input("Date: ")))

    print(f"Historical:  {historical_sales_avg[date_to_get]:.2f}")
    print(f"Predicted:  {projected_avg_sales(date_to_get):.2f}")
    print()
    print(f"Historical with Weather:  {(historical_sales_avg[date_to_get] * weather_effect):.2f}")
    print(f"Predicted with Weather:  {(projected_avg_sales(date_to_get) * weather_effect ):.2f}")

    domain = range(len(historical_sales_avg))
    plot_data(domain, historical_sales_avg, projected_avg_sales)


def date_to_day(date_input: str):
    year = 2022
    date = datetime.strptime(date_input, f'%m-%d-%Y').date()
    day_of_year = date.timetuple().tm_yday
    return day_of_year


def read_data(data_file, model_file):
    sales = []
    model = []

    with open(data_file, 'rb') as f:
        sales = pickle.load(f)
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    return sales, model


def plot_data(domain, function, model):
    line = np.linspace(1, len(domain), len(domain))
    plt.plot(domain, function)
    plt.plot(line, model(line), color="red")
    plt.show()


if __name__ == "__main__":
    main()
