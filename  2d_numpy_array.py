# Import numpy
import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]


# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# OUTPUT
# <class 'numpy.ndarray'>
# (4, 2)
# Print out the 50th row of np_baseball
print("Subsetting 2D NumPy Arrays: ", np_baseball[3, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_kg = np_baseball[:, 1]
print("Subsetting 2D NumPy Arrays: ", np_weight_kg)

# updated is available as 2D numpy array
updated = np.array([[150, 79.4],
                    [216, 103.7],
                    [211, 99.5],
                    [189, 76.2]])

# Print out addition of np_baseball and updated
print("2D Adding Arithmetic: ", np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592])

# Print out product of np_baseball and conversion
print("2D Multiply Arithmetic: ", np_baseball * conversion)

# Explore the baseball data
# Because the mean and median are so far apart, you decide to complain to the MLB. They find the error and send the corrected data over to you. It's again available as a 2D Numpy array np_baseball, with three columns.

# The Python script on the right already includes code to print out informative messages with the different summary statistics.
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))
