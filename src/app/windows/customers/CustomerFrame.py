import tkinter as tk
from tkinter import ttk
from src.parsing.DataReader import DataReader
import os
import pickle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

CLOVER_CSV_CUSTOMER_NAME = 16


class CustomerFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = self.load_or_compute_cust_data()
        self.create_figure()

    @staticmethod
    def load_or_compute_cust_data():
        pickle_file = os.path.join('dataset', 'cust_to_sales_dict.pkl')

        if os.path.exists(pickle_file):
            # If pickle file exists, load the data from it
            with open(pickle_file, "rb") as f:
                cust_to_sales_dict = pickle.load(f)
        else:
            # if pickle file doesn't exist, compute the data and save it to the pickle file
            data_path = os.path.join('dataset', 'dataSet.csv')
            reader = DataReader(data_path)
            cust_list = reader.get_field(CLOVER_CSV_CUSTOMER_NAME)

            cust_to_sales_dict = {}

            for name in cust_list:
                if name == '' or name == 'MANUALLY ENTERED' or name == 'A GIFT FOR YOU':
                    continue

                try:
                    cust_to_sales_dict[name] += 1
                except KeyError:
                    cust_to_sales_dict[name] = 1  # start from 1 instead of 0

            # sort the dictionary by values
            cust_to_sales_dict = dict(sorted(cust_to_sales_dict.items(), key=lambda item: item[1], reverse=True))

            # save to pickle
            with open(pickle_file, "wb") as f:
                pickle.dump(cust_to_sales_dict, f)

        return cust_to_sales_dict

    def create_figure(self):
        number_of_customers_to_display = 20  # number of top customers to display

        # create plot
        fig = Figure(figsize=(5.4, 5.4), dpi=100, tight_layout=True)
        ax = fig.add_subplot(111)

        # extract the data for customers
        top_cust_names = list(self.data.keys())[:number_of_customers_to_display]
        top_cust_sales = list(self.data.values())[:number_of_customers_to_display]

        # create the bar plot
        bars = ax.barh(top_cust_names, top_cust_sales, color='blue')
        ax.set_xlabel('Number of Sales')
        ax.set_ylabel('Customer Names')
        ax.set_title('Top {} Customers by Sales'.format(number_of_customers_to_display))

        # rotate labels for readability
        for label in ax.get_xticklabels():
            label.set_rotation(45)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return None
