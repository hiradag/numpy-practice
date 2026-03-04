import numpy as np
#BROADCASTING:--  Broadcasting means NumPy automatically adjusts array shapes so that arithmetic operations can happen between arrays of different shapes.


a = np.array([1,2,3])
b = 10
print(a + b)
#NumPy automatically stretched 10 to: [10 10 10]

c = np.array([[1,2,3],[4,5,6]])
d = np.array([10,20,30])
print(c+d)
#NumPy stretches b row-wise: [[10 20 30] [10 20 30]]


#Two arrays are compatible if: Their dimensions are equal OR  One of them is 1
#NumPy checks shape from right to left



#WORKING WITH MISSING VALUES  isnan()

k=np.array([1,2,3,4,np.nan,6])
print(k)

#TO REMOVE MISSING /NAN VALUES FROM ARRAY

print(k[~np.isnan(k)])


#SORTING

#FOR 1D ARRAY
j=np.random.randint(10,size=10)
print(j)
print(np.sort(j))

#FOR 2D ARRAY
i=np.random.randint(1,100,24).reshape(6,4)
print(i)
print(np.sort(i))   #ROWWISE SORTING
print(np.sort(i,axis=0))   #COLUMNWISE SORTING

#TO SORT IN DECREASING ORDER 
print(np.sort(j)[::-1])


#APPEND
#np.append() is used to add elements to an array.It does NOT modify original array and It returns a new array

v = np.array([1,2,3])
u = np.append(v, 4)
print(u)
t = np.append(v, 8)
print(t)   # append doest not modify the original array
x =print(np.append(v, [4,5,6]))
