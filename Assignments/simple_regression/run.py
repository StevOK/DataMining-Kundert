# Steven Kundert
# CMPS 5443 - Griffin
# Assignment 3 - Simple Linear Regression
# 9/20/17
# This program reads a csv of mortgage rates and median home prices by year,
# stores that information in a matrix using pandas, cleans up the values,
# then plots the points with the year as the x-axis and median house price as
# the y-axis. It also performs a simple linear regression on on those points,
# then plots the line generated from the coefficients from the regression

import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

# Read the csv and store as a matrix using pandas
# This was the best workaround I could find since the csv had
#  commas in the price fields
data = pd.io.parsers.read_csv("mortgage_rates.csv").as_matrix()

# Take out the dollar signs and commas from the home prices
for item in data:
    item[2] = int(item[2].replace('$','').replace(',',''))
    
# Create arrays for the x and y axis values
x = data[:,0]
y = data[:,2]

# Convert all the x and y values to Python numbers rather than Sage
# Was causing a dumb error
x = pd.to_numeric(x)
y = pd.to_numeric(y)

# Plot the data points
plt.scatter(x, y, s=10)

# Write labels for the table, make the table center around the data
plt.title("Median Home Prices from 1988 to 2003")
plt.xlabel("Year")
plt.ylabel("Median Home Price ($)")
plt.autoscale(tight=True)

# Run the linear regression. I used polynomial degree 3 in this case
#  because it fits better than 1 or 2
z = sp.polyfit(x,y,3)

# Create a mathematical function so that the linear regression can be plotted
f = sp.poly1d(z)

# Make a bunch of x points in the same range as the data plot
fx = sp.linspace(1988,2003,1000)

# Plot the line of the regression using the x points we just made
#  and the function for the regression
plt.plot(fx, f(fx), linewidth=2)

# Display both plots
plt.show()
