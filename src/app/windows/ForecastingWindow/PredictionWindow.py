import os
import tkinter as tk
from tkinter import ttk
import src.app.gui_constants as GUI
from src.app.windows.ForecastingWindow.PredictionStyle import configure_style
from src.predictions.DataForecaster import DataForecaster
from src.predictions.salesPrediction import plot_data
from src.utils.weather_utils import month_to_int, date_to_day
from src.utils.file_utils import check_files


class PredictionPanel(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        check_files()

        # Initialize instance attributes
        self.selected_month = None
        self.month_menu = None
        self.selected_weather = None
        self.weather_menu = None
        self.selected_day = None
        self.day_box = None
        self.button = None

        configure_style()

        self.create_widgets()

    def create_widgets(self):
        """Create and pack all widgets in the frame."""

        # Frame to hold all widgets
        widget_frame = ttk.Frame(self)
        widget_frame.pack(expand=True)

        # Month option menu
        self.selected_month = tk.StringVar()
        self.month_menu = self.create_option_menu(widget_frame, self.selected_month, GUI.MONTHS)

        # Weather option menu
        self.selected_weather = tk.StringVar()
        self.weather_menu = self.create_option_menu(widget_frame, self.selected_weather, GUI.WEATHER_LEVELS)

        # Day input
        self.selected_day = tk.StringVar()
        self.create_label_entry(widget_frame, "Day: ", self.selected_day)

        # Forecast button
        self.button = ttk.Button(widget_frame, text="Forecast!", command=self.forecast_from_selected)
        self.button.pack(pady=10)

    @staticmethod
    def create_option_menu(parent, variable, options):
        """Create an OptionMenu with the provided options."""
        menu = ttk.OptionMenu(parent, variable, options[0], *options)
        menu.pack(pady=10)
        return menu

    @staticmethod
    def create_label_entry(parent, label_text, variable):
        """Create a Label and Entry pair."""
        day_label = ttk.Label(parent, text=label_text, style='TLabel')
        day_label.pack()

        entry = ttk.Entry(parent, textvariable=variable, font=('Helvetica', 12, 'bold'))
        entry.pack(pady=5, padx=100)

    def forecast_from_selected(self):
        """Forecast from the selected values and plot the results."""
        print(f"{self.selected_month.get()} {self.selected_day.get()}, {self.selected_weather.get()}")

        hist_file_path = os.path.join('dataset', 'serialized', 'sales_data.pkl')
        cont_file_path = os.path.join('dataset', 'serialized', 'model.pkl')

        data_tup = (hist_file_path, cont_file_path)
        forecaster = DataForecaster(data_tup)

        result = forecaster.forecast(
            month_to_int(self.selected_month.get()),
            self.selected_day.get(),
            self.selected_weather.get(),
        )

        print(result)

        result_window = tk.Toplevel(self)

        plot_data(
            range(len(forecaster.get_historical_model())),
            forecaster.get_historical_model(),
            forecaster.get_cont_model(),
            date_to_day(f'{month_to_int(self.selected_month.get())}-{self.selected_day.get()}-2022')
        )


