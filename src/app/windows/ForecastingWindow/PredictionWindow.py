import tkinter as tk
from tkinter import ttk
import src.app.gui_constants as GUI
from src.app.windows.ForecastingWindow.PredictionStyle import configure_style


class PredictionPanel(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        style = configure_style()

        # Create a new frame that will contain all your widgets
        widget_frame = ttk.Frame(self)
        widget_frame.pack(expand=True)  # Expand the frame to fill the parent

        self.selected_month = tk.StringVar()
        self.month_menu = ttk.OptionMenu(widget_frame, self.selected_month, GUI.MONTHS[0], *GUI.MONTHS)
        self.month_menu.pack(pady=10)

        self.selected_weather = tk.StringVar()
        self.weather_menu = ttk.OptionMenu(widget_frame, self.selected_weather, GUI.WEATHER_LEVELS[0],
                                           *GUI.WEATHER_LEVELS)
        self.weather_menu.pack(pady=10)

        self.selected_day = tk.StringVar()

        # Add a label before the Entry widget
        day_label = ttk.Label(widget_frame, text="Day: ", style='TLabel')
        day_label.pack()

        self.day_box = ttk.Entry(widget_frame, textvariable=self.selected_day, font=('Helvetica', 12, 'bold'))
        self.day_box.pack(pady=5, padx=100)

        self.button = ttk.Button(widget_frame, text="Click me!", command=self.forecast_from_selected)
        self.button.pack(pady=10)

    def forecast_from_selected(self):
        print(f"{self.selected_month.get()} {self.selected_day.get()}, {self.selected_weather.get()}")
