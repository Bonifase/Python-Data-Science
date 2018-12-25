'''
Numeric Python
Alternative to Python list: NumPy Array
calculations over entire array
easy and fast
numpy, a powerful package to do data science.
'''
# Import the numpy package as np
import numpy as np
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

# height and weight are available as regular lists
height_in = [180, 160, 175, 190, 188, 176, 150, 200]
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200]

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2
print(bmi)

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print("Light: ", light)

# Print out BMIs of all baseball players whose BMI is below 21
print("Lightweight baseball players: ", bmi[light])


print("Adding numpy list: ", np.array([True, 1, 2]) + np.array([3, 4, False]))

# OUTPUT
# Light:  [ True  True  True  True  True  True  True  True]
# Lightweight baseball players:
# [3.90593892 5.90468111 4.82104461 4.0898751  3.73972876 3.99471026
#  6.53072988 3.51534503]
# Adding numpy list:  [4 5 2]

# Print out the weight at index 2
print("Subsetting NumPy Arrays at index 2: ", np_weight_kg[2])

# Print out sub-array of np_height: index 3 up to and including index 7
print("Subsetting NumPy Arrays from index 3 to 7: ", np_height_m[3:7])

# Print out the weight at index 3
print("Subsetting NumPy Arrays at index 3: ", np_weight_kg[3])

# Print out sub-array of np_height: index 6 up to and including index 7
print("Subsetting NumPy Arrays from index 6 to 7: ", np_height_m[6:7])
