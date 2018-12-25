# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

year = [2000, 2001, 2002, 2003]
pop = [15000, 17000, 17500, 14500]

# Print the last item from years and populations
print(year[-1])
print(pop[-1])

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show(block=True)

# Build Scatter plot
plt.scatter(year, pop)

# Show plot
plt.show()

# Build a histogram
# Create histogram of pop data
plt.hist(pop)

# Display histogram
plt.show()

# Build histogram with 5 bins
plt.hist(pop, bins=5)

# Show and clear plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(pop, bins=20)

# Show and clear plot again
plt.show()
plt.clf()
