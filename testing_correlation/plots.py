import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
from scipy.stats import probplot

def plot_residuals_vs_fitted(y_pred, residuals):
    plt.figure(figsize=(6, 4))
    sns.residplot(x=y_pred, y=residuals, lowess=True, line_kws={'color': 'red'})
    plt.xlabel("Fitted Values")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Fitted")
    plt.axhline(0, color='black', linestyle='dashed')
    plt.show()

def plot_qq(residuals):
    plt.figure(figsize=(6, 4))
    probplot(residuals, dist="norm", plot=plt)
    plt.title("Q-Q Plot")
    plt.show()

def plot_scale_location(y_pred, residuals):
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=y_pred, y=np.sqrt(np.abs(residuals)))
    plt.xlabel("Fitted Values")
    plt.ylabel("√|Residuals|")
    plt.title("Scale-Location Plot")
    plt.axhline(0, color='black', linestyle='dashed')
    plt.show()

def plot_histogram(residuals):
    plt.figure(figsize=(6, 4))
    plt.hist(residuals, bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    plt.title("Histogram of Residuals")
    plt.show()

def plot_regression_line(X, y, model):
    slope = model.coef_[0]
    intercept = model.intercept_
    x_range = [X.min().values[0], X.max().values[0]]
    y_range = [slope * x + intercept for x in x_range]
    
    plt.scatter(X, y, color='blue', label="Actual Data")
    plt.plot(x_range, y_range, color='red', linewidth=2, label="Regression Line")
    plt.xlabel("Education Level")
    plt.ylabel("Income")
    plt.title("Regression Line Plot")
    plt.legend()
    plt.show()

def plot_residuals_vs_order(residuals):
    plt.figure(figsize=(6, 4))
    plt.plot(residuals.values, marker='o', linestyle='-')
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel("Observation Order")
    plt.ylabel("Residuals")
    plt.title("Residuals vs Order")
    plt.show()