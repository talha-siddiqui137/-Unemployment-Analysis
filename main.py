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

#Removes extra spaces from column names.
new_df.columns = new_df.columns.str.strip()

new_df['Date'] = pd.to_datetime(new_df['Date'])


#line chart
monthly = new_df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))
plt.plot(monthly.index, monthly.values, marker='o')
plt.title("Average Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(color= 'gray', linestyle=':')
plt.show()


# bar chart

region = new_df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print(region)

plt.figure(figsize=(10,8))
plt.barh(region.index, region.values, color='purple')
plt.title("Average Unemployment by Region")
plt.xlabel("Average Unemployment")
plt.ylabel("Region")
plt.grid( linestyle=':')
plt.show()