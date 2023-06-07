import tkinter as tk
from tkinter import ttk
import src.app.gui_constants as GUI
from src.visualizations.SineRegressionVisual import compute_sine_visual


class StatsWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a ttk.Button instead of a tk.Button
        self.sine_visual_btn = ttk.Button(self, text="View Sine Visual (this may take a second)",
                                          command=self.display_sine_stats)
        # Set the layout for the button
        self.sine_visual_btn.pack()

    def display_sine_stats(self):
        compute_sine_visual()