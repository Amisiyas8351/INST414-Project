from dataset import load_data
from modeling.train import train_model
from plots import plot_residuals_vs_fitted, plot_qq, plot_scale_location, plot_residuals_vs_leverage, plot_histogram, plot_regression_line
from correlation import calculate_p_value

#Load data
df = load_data('data/processed/education_income.csv')

#Defining the independent (X) and dependent (y) variables
X = df[['education level']]
y = df['income']

#Training the model
model = train_model(X, y)

#Predictions and residuals
y_pred = model.predict(X)
residuals = y - y_pred

#Calling plot functions
plot_residuals_vs_fitted(y_pred, residuals)
plot_qq(residuals)
plot_scale_location(y_pred, residuals)
plot_residuals_vs_leverage(X, y)
plot_histogram(residuals)
plot_regression_line(X, y, model)

#Calculating p-value (F-test)
p_value = calculate_p_value(y, y_pred, residuals, X)
print(f"P-Value: {p_value}")