import numpy as np

a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(27).reshape(3,3,3)


#INDEXING ------------

print(a1[-1])
print(a1[0])
print(a2[1,0])
print(a2[1,2])
print(a2[2,3])
print(a3[0,1,0])
print(a3[0,0,0])


#SLICING-----------------

#a1[a,b,c]  a=start b=end c=steps  a=included  b=excluded    IN 1D ARRAY
#a2[ : : , : : ]  (ROW from: Row to: steps , COL from: COL to: steps)    IN 2D ARRAY
#a3[which block of array,row,col]   IN 3D ARRAY

print(a1[2:5])
print(a1[2:5:2])

print(a2[0,:])
print(a2[:,2])
print(a2[1: , 1:3])
print(a2[: :2,::3])
print(a2[::2,1::2])
print(a2[1,::3])

print(a3[1])
print(a3[::2])
print(a3[0,1,:])
print(a3[1,:,1])
print(a3[2,1:,1:])



#ITERATING------------------------------------------

# for i in a1:
#     print(i)
# for i in a2:
#     print(i)      These will return array in their normal or original form
# for i in a3:
#     print(i)   

#IF WE WANT TO PRINT ALL ARRAY IN 1D , BY FIRST CONVERTING THEM TO 1D FROM THEIR USUAL FORM
for i in np.nditer(a3):
    print(i)
for i in np.nditer(a2):
    print(i)
    

# Transpose (row->col and col->row)
#Ravel(convert N-d array to 1d array)

print(np.transpose(a2))
print(a2.ravel())


#STACKING --------Combining two or more arrays in a single array  -----Horizontal/Vertical
#hstack → Horizontal → Side by side
#vstack → Vertical → One below another

a4=np.array([[1,2,3],[4,5,6]])
a5=np.array([[9,10,11],[12,13,14]])
print(np.hstack((a4,a5)))
print(np.vstack((a4,a5)))
     

#SPLIT----------------------------------------

a7 = np.array([1,2,3,4,5,6])
result = np.split(a7, 3)
print(result)

a8 = np.array([[1,2,3,4], [5,6,7,8]])
print(np.hsplit(a8, 2))

print(np.vsplit(a8, 2))


#FANCY INDEXING:--Fancy Indexing in NumPy is a method of selecting specific rows or columns using a list or array of index positions instead of slices.----------------------------------------------------------------------

a9=np.arange(24).reshape(6,4)

#SELECTING SPECIFIC ROWS
print(a9[[0,2,3,5]])

#SELECTING SPECIFIC COLUMNS
print(a9[:, [0,2,3]])

#--------------------------------------------------------------------------------------------------------------

#BOOLEAN INDEXING: Boolean indexing means selecting elements using conditions
a10= np.random.randint(1,100,24).reshape(6,4)
print(a10)

print(a10[a10 > 50])
print(a10[a10 % 2==0])
print(a10[(a10>50) & (a10%2==0)])





