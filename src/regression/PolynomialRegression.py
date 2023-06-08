from scipy.optimize import curve_fit
import numpy as np


class PolynomialRegression:
    def __init__(self, domain, function):
        self.domain = domain
        self.function = function

    def fit_polynomial(self, degree: int):
        return np.polyfit(self.domain, self.function, degree)
