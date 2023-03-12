import random
import pandas as pd
from datetime import datetime, timedelta

# Set the start and end date of the data
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 31)
# Generate a list of dates
date_list = [(start_date + timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S') for i in range((end_date - start_date).days * 24)]

# Generate random energy consumption data for each hour
consumption = [random.uniform(0, 5) for _ in range(len(date_list))]

# Create a DataFrame from the data
df = pd.DataFrame({'Date': date_list, 'Consumption': consumption})

# Save the DataFrame to a CSV file
df.to_csv('energy_consumption.csv', index=False)
