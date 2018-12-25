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
