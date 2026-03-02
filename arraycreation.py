import numpy as np

a=np.arange(1,11)
print(a) 

b=np.arange(1,11,2)
print(b)

# With reshaping  (m*n) m= rows and n= columns

c = np.arange(1,11).reshape(2,5)
print(c)
  
# Initializing values with zeros or ones or Random values

d=np.zeros((3,4))
e=np.ones((4,5))
f=np.random.random((3,4))
print(d)
print(e)
print(f)

# linearly space or equidistant 

g= np.linspace(-10,10,10)
print(g)

# Identity Matrix
h=np.identity(3)
print(h)


