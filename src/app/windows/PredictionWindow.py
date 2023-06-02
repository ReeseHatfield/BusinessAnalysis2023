import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]

weather_effect_levels = [
    'None',
    'Light',
    'Moderate',
    'Heavy',
]


class PredictionPanel(ttk.Frame):  # inherit from ttk.Frame
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.selected_month = tk.StringVar()
        self.month_menu = ttk.OptionMenu(self, self.selected_month, months[0], *months)
        self.month_menu.pack()

        self.selected_weather = tk.StringVar()
        self.weather_menu = ttk.OptionMenu(self, self.selected_weather, weather_effect_levels[0],
                                           *weather_effect_levels)
        self.weather_menu.pack()

        self.selected_day = tk.StringVar()
        self.day_box = tk.Entry(self, textvariable=self.selected_day, font=('calibre', 10, 'bold'))
        self.day_box.pack()

        self.button = ttk.Button(self, text="Click me!", command=self.forecast_from_selected)
        self.button.pack()

    def forecast_from_selected(self):
        print(f"{self.selected_month.get()} {self.selected_day.get()}, {self.selected_weather.get()}")


