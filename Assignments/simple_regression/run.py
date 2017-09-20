# Steven Kundert
# CMPS 5443 - Griffin
# Assignment 3 - Simple Linear Regression
# 9/20/17
#
# This is Franken-code that needs to be cleaned up and documented
#
#

#import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#import csv
import pandas as pd

#def error(f,x,y):
#    return sp.sum((f(x)-y)**2)

np_array = pd.io.parsers.read_csv("mortgage_rates.csv").as_matrix()
for item in np_array:
    item[2] = int(item[2].replace('$','').replace(',',''))
    
data = pd.DataFrame(np_array)

print(data)

x = np_array[:,0]
y = np_array[:,2]
#z = np_array[:,2]
x = pd.to_numeric(x)
y = pd.to_numeric(y)



plt.scatter(x, y, s=10)
plt.title("Median Home Prices from 1988 to 2003")
plt.xlabel("Year")
plt.ylabel("Median Home Price ($)")
plt.autoscale(tight=True)
z = sp.polyfit(x,y,3)
f = sp.poly1d(z)
fx = sp.linspace(1988,2003,1000)
plt.plot(fx, f(fx), linewidth=2)
plt.show()
