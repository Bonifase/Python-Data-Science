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
# Because the mean and median are so far apart,
# you decide to complain to the MLB.
# They find the error and send the corrected data over to you.
# It's again available as a 2D Numpy array np_baseball, with three columns.

# The Python script on the right already includes code
# to print out informative messages with the different summary statistics.
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


# Convert heights and positions,
# which are regular lists, to numpy arrays.
# Call them np_heights and np_positions.
# Extract all the heights of the goalkeepers.
# Extract all the heights of all the other players.
# This time use np_positions != 'GK' as an index for np_heights.
# Assign the result to other_heights.
# Print out the median height of the goalkeepers
# using np.median(). Replace None with the correct code.
# Do the same for the other players.
# Print out their median height. Replace None with the correct code.

positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
