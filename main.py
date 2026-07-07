import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Unemployment in India.csv")

# dropna() removes any row that has even one missing value.
# dropna(how='all') removes only rows where every column is missing.

new_df = df.dropna(how='all')

print(new_df.info())
print(new_df.isnull().sum())


print(new_df.describe())

print(new_df['Region'].value_counts())

new_df.columns = new_df.columns.str.strip()

new_df['Date'] = pd.to_datetime(new_df['Date'])

print(new_df.info())
print(new_df.head())