import pickle
import os
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from src.constants import _weather_effect
from src.app.windows.MainWindow import MainWindow


def main():
    root = tk.Tk()

    customized_style = ttk.Style()
    customized_style.configure('Custom.TNotebook.Tab', padding=[12, 12], font=('Helvetica', 10))
    customized_style.configure('Custom.TNotebook', tabposition='wn')

    app = MainWindow(root)
    root.mainloop()


def read_data(data_file, model_file):
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
