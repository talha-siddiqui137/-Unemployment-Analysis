# TASK : Unemployment Analysis with Python 

# ● Analyze unemployment rate data representing unemployed people percentage. 
# ● Use Python for data cleaning, exploration, and visualization of unemployment trends. 
# ● Investigate the impact of Covid-19 on unemployment rates. 
# ● Identify key patterns or seasonal trends in the data. 
# ● Present insights that could inform economic or social policies. 

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

region = region.sort_values()

plt.figure(figsize=(10,8))
plt.barh(region.index, region.values, color='purple')
plt.title("Average Unemployment by Region")
plt.xlabel("Average Unemployment")
plt.ylabel("Region")
plt.grid(axis='x', linestyle=':')
plt.show()


#histogram 

plt.figure(figsize=(8,5))
plt.hist(new_df['Estimated Unemployment Rate (%)'], bins=15, color= 'orange', edgecolor= 'black')

plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.grid(linestyle=':', axis='x')

plt.show()

# Investigate Covid-19 impact

# Average unemployment rate over time
covid = new_df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,5))

# Plot the full timeline
plt.plot(covid.index, covid.values, marker='o', label='Average Unemployment Rate')

# Highlight the start of Covid-19
plt.axvline(pd.Timestamp('2020-03-01'),
            color='red',
            linestyle='--',
            linewidth=2,
            label='Covid-19 Begins (March 2020)')

plt.title("Average Unemployment Rate Before and During Covid-19")
plt.xlabel("Date")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(linestyle=':')
plt.legend()

plt.show()




print("Average unemployment rate:",
      round(new_df['Estimated Unemployment Rate (%)'].mean(), 2))

print("Highest unemployment rate:",
      new_df['Estimated Unemployment Rate (%)'].max())

print("Lowest unemployment rate:",
      new_df['Estimated Unemployment Rate (%)'].min())


# idxmax() stands for Index of Maximum.

# It returns the label (index) where the maximum value occurs.

highest_region = region.idxmax()
highest_rate = region.max()

lowest_region = region.idxmin()
lowest_rate = region.min()

print(f"Highest average unemployment region: {highest_region} ({highest_rate:.2f}%)")
print(f"Lowest average unemployment region: {lowest_region} ({lowest_rate:.2f}%)")