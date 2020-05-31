#TODO:


import numpy as np 

a = np.array([4, 5, 53, 23, 23])
##printing the number of dimensions of the array
print(a.ndim)
##printing the shape of the array
print(a.shape)

b = np.array([[34, 35, 56, 2, 6],
            [12, 32, 5, 4, 56]])
##printning the number of dimensions of the array
print(b.ndim)
##print the shape of the array
print(b.shape)

c = np.array([[[23, 34, 45, 3], [4, 56, 67, 67]],
            [[12, 34, 45, 3], [54,  70, 10, 23]]])

print(c.ndim)
print(c.shape)