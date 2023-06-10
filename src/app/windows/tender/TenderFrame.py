import tkinter as tk
from tkinter import ttk
import os
import pickle

from src.parsing.DataReader import DataReader

CLOVER_CSV_TENDER_TYPE = 7


class TenderFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.data = self.load_or_compute_tender_data()

    @staticmethod
    def load_or_compute_tender_data():
        pickle_file = os.path.join('dataset', 'tender_list.pkl')

        data_path = os.path.join('dataset', 'dataSet.csv')

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
            'Gift Cards': 0,
            'External Gift Card': 0,
            'Gift Card ': 0
        }

        for sale in tender_list:
            type_to_sales[sale] += 1

        print(type_to_sales)

