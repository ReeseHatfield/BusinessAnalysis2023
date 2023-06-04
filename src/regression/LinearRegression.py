import numpy as np


class LinearRegression:
    def __init__(self):
        self.coefficients = None

    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1)  # add a column of 1s for the intercept
        self.coefficients = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)  # add a column of 1s for the intercept
        return X @ self.coefficients

    def get_coeffs(self):
        return self.coefficients
