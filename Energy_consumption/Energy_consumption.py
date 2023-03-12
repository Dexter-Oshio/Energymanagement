import pandas as pd
import matplotlib.pyplot as plt

# Load energy consumption data from a CSV file
df = pd.read_csv('energy_consumption.csv')

# Convert the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' column as the index
df.set_index('Date', inplace=True)

# Resample the data to hourly frequency and calculate the average consumption for each hour
hourly_avg = df.resample('H').mean()

# Plot the hourly average consumption
plt.plot(hourly_avg.index, hourly_avg['Consumption'])
plt.xlabel('Date')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Hourly Energy Consumption')
plt.show()

# Calculate the daily total consumption
daily_total = df.resample('D').sum()

# Plot the daily total consumption
plt.plot(daily_total.index, daily_total['Consumption'])
plt.xlabel('Date')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Daily Energy Consumption')
plt.show()

# Calculate the monthly total consumption
monthly_total = df.resample('M').sum()

# Plot the monthly total consumption
plt.plot(monthly_total.index, monthly_total['Consumption'])
plt.xlabel('Date')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Monthly Energy Consumption')
plt.show()
