# Written by ChatGPT-3.5

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Function to parse CSV files
def parse_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
            except ValueError:
                date = datetime.strptime(row[0], '%Y')
            value = float(row[1])
            data.append((date, value))
    return data

# Parse CSV files
earnings_data = parse_csv('Median Weekly Nominal Earnings.csv')
gold_data = parse_csv('OzGold-USD Price History.csv')

# Calculate earnings in terms of ounces of gold
earnings_oz_gold = []
for earnings_entry in earnings_data:
    earnings_date, earnings_value = earnings_entry
    for gold_entry in gold_data:
        gold_date, gold_price = gold_entry
        if gold_date.year == earnings_date.year:
            earnings_in_gold = earnings_value / gold_price
            earnings_oz_gold.append((earnings_date, earnings_in_gold))
            break

# Sort the data by date
earnings_oz_gold.sort(key=lambda x: x[0])

# Extract dates and values for plotting
dates = [entry[0] for entry in earnings_oz_gold]
values = [entry[1] for entry in earnings_oz_gold]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(dates, values, marker='o', linestyle='-')
plt.title('Median Weekly Nominal Earnings in Ounces of Gold')
plt.xlabel('Year')
plt.ylabel('Ounces of Gold')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

