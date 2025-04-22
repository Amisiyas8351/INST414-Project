from dataset import load_data
from modeling.train import train_model
from plots import plot_residuals_vs_fitted, plot_qq, plot_scale_location, plot_histogram, plot_regression_line, plot_residuals_vs_order

from correlation import calculate_p_value
import numpy as np
from sklearn.metrics import r2_score

#Load data
df = load_data('data/processed/education_income.csv')

#Defining the independent (X) and dependent (y) variables
X = df[['education level']]
y = np.log(df['income'])

#Training the model
model = train_model(X, y)

#Predictions and residuals
y_pred = model.predict(X)
residuals = y - y_pred

#Calling plot functions
plot_residuals_vs_fitted(y_pred, residuals)
plot_qq(residuals)
plot_scale_location(y_pred, residuals)
plot_histogram(residuals)
plot_regression_line(X, y, model)
plot_residuals_vs_order(residuals)

#Calculating p-value (F-test)
p_value = calculate_p_value(y, y_pred, residuals, X)
print(f"P-Value: {p_value}")

n = len(y)
k = X.shape[1]
SSR = np.sum((y_pred - np.mean(y))**2)
SSE = np.sum(residuals**2)
F_statistic = (SSR / k) / (SSE / (n - k - 1))
r2 = r2_score(y, y_pred)

print("F-statistic =", F_statistic)
print("R-squared =", r2)