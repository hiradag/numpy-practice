import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)

# (m,n,p) m=divided in how many blocks n=rows p=columns
a3=np.arange(8).reshape(2,2,2)

# ndim  (tells how many dimensions does array have)
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

# Shape (Items in each dimension)
print(a1.shape)
print(a2.shape)
print(a3.shape)

#Size (Number of Item)
print(a1.size)
print(a2.size)
print(a3.size)

#dtype(item's data type)
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

#item size (every item's memory)
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)


# Changing datatype 
#  astype
