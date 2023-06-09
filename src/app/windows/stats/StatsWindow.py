import tkinter as tk
from tkinter import ttk
from src.visualizations.SineRegressionVisual import compute_sine_visual
from src.visualizations.LinearRegressionVisual import compute_linear_visual


class StatsWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Custom Style configuration
        self.style = ttk.Style()
        self.style.configure("StatsWindow.TButton",
                             foreground="black",
                             background="white",
                             font=("Helvetica", 12),
                             padding=10)

        self.style.configure("StatsWindow.TLabel",
                             foreground="black",
                             background="white",
                             font=("Helvetica", 14),
                             padding=10)

        # Create Labels
        self.sine_visual_lbl = ttk.Label(self, text="Sine Regression Visualisation:", style="StatsWindow.TLabel")
        self.sine_visual_lbl.grid(column=0, row=0, sticky=tk.W)

        self.linear_visual_lbl = ttk.Label(self, text="Linear Regression Visualisation:",
                                           style="StatsWindow.TLabel")
        self.linear_visual_lbl.grid(column=0, row=2, sticky=tk.W)

        # Create Buttons
        self.sine_visual_btn = ttk.Button(self, text="View", command=compute_sine_visual,
                                          style="StatsWindow.TButton")
        self.sine_visual_btn.grid(column=1, row=0, sticky=tk.E)

        self.linear_visual_btn = ttk.Button(self, text="View", command=compute_linear_visual,
                                            style="StatsWindow.TButton")
        self.linear_visual_btn.grid(column=1, row=2, sticky=tk.E)

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)
