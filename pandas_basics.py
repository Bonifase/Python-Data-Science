# Import pandas as pd
import pandas as pd

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India',
         'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Build cars
# DataFrame Data frame to dictionary
names = ['United States',
         'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)


# CSV to DataFrame (1)
# Putting data in a dictionary and then building a DataFrame works,
# but it's not very efficient.
# What if you're dealing with millions of observations?
# In those cases, the data is typically available as files
# with a regular structure. One of those file types is the CSV file,
# which is short for "comma-separated values".

# To import CSV data into Python as a Pandas DataFrame you can use read_csv()
# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print("cars", cars)
