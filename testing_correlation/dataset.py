import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

file_path = 'data/processed/education_income.csv'
df = load_data(file_path)

print(df.head())