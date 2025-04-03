import numpy as np
from scipy.stats import f

def calculate_p_value(y, y_pred, residuals, X):
    n = len(y)
    k = X.shape[1]
    SSR = np.sum((y_pred - np.mean(y))**2)
    SSE = np.sum(residuals**2)
    F_statistic = (SSR / k) / (SSE / (n - k - 1))
    p_value = 1 - f.cdf(F_statistic, k, n - k - 1)
    return p_value