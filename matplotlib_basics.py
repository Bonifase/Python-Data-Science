# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Import numpy as np
import numpy as np

life_exp = [40, 70, 100, 45]
gdp_cap = [400, 200, 400, 300]
year = [2000, 2001, 2002, 2003]
pop = [15000, 17000, 17500, 14500]
continents = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'black'
}


# Print the last item from years and populations
print(year[-1])
print(pop[-1])

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# adding labels to axes
plt.ylabel("Population")
plt.xlabel("Year")

# adding title
plt.title("World Population projection")

# customizing axis scale
plt.yticks([0, 1, 2, 3, 4, 5],
           [
               "0 bilion",
               "1 billion",
               "2 billion",
               "3 billion",
               "4 billion",
               "5 billion"])

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


# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s=np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Display the plot
plt.show()

# Specify c and alpha inside plt.scatter()
plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2, c=col, alpha=0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Show the plot
plt.show()

# Scatter plot
plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2, c=col, alpha=0.8)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
