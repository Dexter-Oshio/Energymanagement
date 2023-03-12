# Energy Consumption Analysis
This code loads energy consumption data from a CSV file, processes it to get hourly average, daily and monthly total consumption and plots the data using pandas and matplotlib.

# Prerequisites
* Python 3.x
* pandas library
* matplotlib library
# Installation
Install Python 3.x from https://www.python.org/downloads/
Install pandas and matplotlib using pip command:
```bash
pip install pandas matplotlib
```
# Usage
Prepare the CSV file containing energy consumption data with columns Date and Consumption.
Update the CSV filename in the code pd.read_csv('energy_consumption.csv') with the appropriate file path.
# Run the code using a Python IDE or from the command line:
```bash
python energy_consumption.py
```
# Outputs
This code generates three plots:
* Hourly Energy Consumption - a line plot of the hourly average consumption over the entire time range.
* Daily Energy Consumption - a line plot of the daily total consumption over the entire time range.
* Monthly Energy Consumption - a line plot of the monthly total consumption over the entire time range.
* Each plot has appropriate labeling and a title to make it easy to understand the data



