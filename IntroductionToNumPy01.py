import numpy as np 

a = np.array([1, 36, 43], dtype = np.int16)
print(a)
print(a.dtype)

'''
converting the values of the array into floats
'''
x = np.array([1, 36, 43], dtype = np.float64)
print(x)
print(x * 2.1)
print(x.dtype)

'''
converting the array values into strings
'''
y = np.array([2, 34, 456, 678, '5'])
print(y)
print(y.dtype)