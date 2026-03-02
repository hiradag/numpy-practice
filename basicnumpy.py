import numpy as np


# Defining 1D array
a= np.array([1,2,3])
print(a)
print(type(a))

#Defining 2D array
b=np.array([[1,2,3],[4,5,6]])
print(b)

#Changing datatype by default it is integer type

c= np.array([1,2,3],dtype=float)
print(c)
print(type(c)) 
# using type function only the data type of elements in array changes not array data type
print(c.dtype)
#dtype is used to see the type of arr or arr's data type