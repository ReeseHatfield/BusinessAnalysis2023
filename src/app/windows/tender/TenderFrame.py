import tkinter as tk
from tkinter import ttk
import os
import pickle

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from src.parsing.DataReader import DataReader

CLOVER_CSV_TENDER_TYPE = 7


class TenderFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = self.load_or_compute_tender_data()
        self.create_figure()

    @staticmethod
    def load_or_compute_tender_data():
        pickle_file = os.path.join('dataset', 'tender_list.pkl')

        if os.path.exists(pickle_file):
            # If pickle file exists, load the data from it
            with open(pickle_file, "rb") as f:
                cust_to_sales_dict = pickle.load(f)
            # early return if data has already been computed
            return cust_to_sales_dict

        data_path = os.path.join('dataset', 'dataSet.csv')
        reader = DataReader(data_path)

        tender_list = reader.get_field(CLOVER_CSV_TENDER_TYPE)

        type_to_sales = {
            'Cash': 0,
            'Debit Card': 0,
            'Credit Card': 0,
            'Gift Cards': 0
        }

        gift_card_sales_names = (
            'Gift Cards', 'External Gift Card', 'Gift Card '
        )

        for sale in tender_list:
            if sale in gift_card_sales_names:

                type_to_sales['Gift Cards'] += 1
            else:
                type_to_sales[sale] += 1

        return type_to_sales

    def create_figure(self):
        fig = Figure(figsize=(5.4, 5.4), dpi=100, tight_layout=True)

        ax = fig.add_subplot(111)

        sales_names = list(self.data.keys())
        sales_numbers = list(self.data.values())

        bars = ax.bar(sales_names, sales_numbers, color='blue')
        ax.set_xlabel('Number of Sales')
        ax.set_ylabel('Sales Type')
        ax.set_title('Sales by type')

        # ax.invert_yaxis()  # Add this line to invert the y-axis

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return None



