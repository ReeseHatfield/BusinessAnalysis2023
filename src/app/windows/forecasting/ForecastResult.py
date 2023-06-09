import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import norm
import numpy as np
from src.predictions.salesPrediction import plot_data
import src.constants.gui_constants as GUI


class ForecastResult(tk.Toplevel):
    def __init__(self, parent, data_tuple: tuple[float, float], domain, function, model, eval_pos=None):
        super().__init__(parent)

        # Calculate stats for data
        self._max = max(data_tuple)
        self._min = min(data_tuple)
        self._mean = (self._max + self._min) / 2
        self._std_dev = (self._max - self._mean) / 2  # standard deviation

        self.label = None
        self.init_label()

        self.init_figure(domain, function, model, eval_pos)

        # move the window at the top center of the screen
        self.geometry("+%d+%d" % (self.winfo_screenwidth() // 2, 0))

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def get_mean(self):
        return self._mean

    def init_label(self):
        min_to_display = f"{(self._min - (self._min * GUI.FORECAST_ERROR_TERM)):.2f}"
        max_to_display = f"{(self._max + (self._max * GUI.FORECAST_ERROR_TERM)):.2f}"
        mean_to_display = f"{self._mean:.2f}"

        self.label = tk.Label(master=self, text=f'Expect sales between {min_to_display} and {max_to_display}, '
                                                f'with a mean of {mean_to_display}', font=GUI.FORECAST_RESULT_FONT)
        self.label.pack()

    def init_figure(self, domain, function, model, eval_pos):
        """ initialize figure and subplots for data visualization. """

        # Create a Matplotlib figure
        fig = Figure(figsize=(10, 4), dpi=GUI.DPI)

        # Create a subplot for the normal distribution
        ax1 = fig.add_subplot(121)

        # Generate values for the x and y axis
        x_values = np.linspace(self._min - 3 * self._std_dev, self._max + 3 * self._std_dev, 100)
        y_values = norm.pdf(x_values, self._mean, self._std_dev)

        # Plot the data and fill the area under the curve
        ax1.plot(x_values, y_values)
        ax1.fill_between(x_values, y_values, color='skyblue', alpha=0.5)

        # Plot vertical lines at the min and max values
        ax1.axvline(x=self._min, color='red', linestyle='--')
        ax1.axvline(x=self._max, color='red', linestyle='--')

        # Create a subplot for the data from plot_data function
        ax2 = fig.add_subplot(122)
        plot_data(ax2, domain, function, model, eval_pos)

        # Create a canvas to display the figure
        canvas = FigureCanvasTkAgg(fig, master=self)

        # Get the widget from the canvas and pack it
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
