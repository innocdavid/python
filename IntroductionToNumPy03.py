#TODO:
"""
Creating arrays with large dimensions
"""

import numpy as np 

##initializing the array with zeros
x = np.zeros((10,10))
##by default the array prints float values
print(x)

y = np.zeros((10, 10), dtype = np.int16)
print(y)

##initializing the array with ones
c = np.ones((10, 10), dtype = np.int16)
print(c)

##initializing the array with fours
c = np.ones((10, 10), dtype = np.int16) * 4
print(c)

##[0 1 2 3 4 5 6 7 8 9 10]
x = np.arange(0, 11, 1)
print(x)

##printing a float sequence
y = np.linspace(0.5, 9.5, num=10)
print(y)

##using the reshape function
print(np.arange(0, 10, 1).reshape((2, 5))) 