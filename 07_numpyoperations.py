import numpy as np

#concatenate:--concatenate() joins two or more arrays. We must specify axis. It does NOT flatten unless axis is not specified in 1D
a=np.array([[0,1,2],[3,4,5]])
b=np.array([[6,7,8],[9,10,11]])

print(np.concatenate((a,b),axis=0))  #ROW CHANGES COLUMN SAME
print(np.concatenate((a,b),axis=1))  #COLUMN CHANGES ROW SAME


#UNIQUE ELEMENTS : np.unique() returns sorted unique elements of an array and by default flattens multi-dimensional arrays into a 1D array.

e=np.array([1,1,2,2,3,3,4,4,5,5,6,6])
f=np.array([[1,2,3,1],[4,8,9,8]])

print(np.unique(e))
print(np.unique(f))

g = np.array([[1,2],[1,2],[3,4]])
print(np.unique(g, axis=0))

#WHERE :--RETURNS THE INDICES OF THE ELEMENT WHICH FULFILS THE CONDITIONS
i=np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,21])
print(np.where(i>50))
print(np.where(i>50,0,i))  #REPLACE ALL GREATER THAN 50 WITH 0 (condition,true,false)

#MIN AND MAX ELEMENTS  : RETURNS INDEX OF MAX/MIN ELEMENTS
print(np.argmax(i))
print(np.argmin(i))


#CUMULATIVE SUM / PERCENTILE 
h=np.array([11,13,15,17,19])

print(np.cumsum(h)) #finds cumulative sum

print(np.percentile(h,90)) #(a,b) a=array variable name   b=who gets this percrntile /how much marks is required for that percentile.

#HISTOGRAM:-- DESCRIBE THE FREQUENCY OF AN ELEMENT IN A SPECIFIC RANGE

z=np.array([11,53,28,50,38,37,94,92,5,30,68,9,78,2,11])
print(np.histogram(z,bins=[0,10,20,30,40,50,60,70,80,90,100]))


#np.isin :-- USED TO SEARCH MUTLIPLE ITEM AT A SINGLE TIME
y=np.array([10,20,30,40,50,60])
items=np.array([10,20,90,100,30])
print(np.isin(y,items))  #np.isin(y, items) checks whether each element of y exists in items.


#np.flip: REVERSE WITH MAINTAINING THE SHAPE

#np.put:  replaces element of the array with the element specified by the user--------------

print(np.put(y,[0,1],[200,300]))  #np.put() modifies the array in-place and returns None.
    #(y,[0,1],[200,300])  y=array,the index of the element we want to replace,the elements
print(y)




#PERMANENT CHANGES:----------
#np.delete:- deletes permanently by taking the index from the user
g=np.array([10,20,30,40])
print(np.delete(g,0))


#np.clip: np.clip() is used to limit (bound) the values of an array within a specified range.
p=np.array([10,20,30,40,70,50,66,98,94])
print(np.clip(p,a_min=20,a_max=80))



#OTHER SET OPERATIONS
# np.intersect1d()	common elements
# np.union1d()	combine unique elements
# np.setdiff1d()	difference between arrays
# np.setxor1d()	elements not common


