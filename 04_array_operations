import numpy as np
# array operations are divided into two parts (scalar and vector)
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

# SCALAR----------------------------------------------------------------------------------------------

#Arithmetic
print(a1*2)

#Relational
print(a2>5)
print(a1>6)

#  VECTOR----------------------------------------------------------------------------------------------

#Arithmetic(IF SAME SIZE)
print(a1+a2)

#max/min/sum/product    AXIS=0(COLUMN-WISE) AXIS=1(ROW-WISE)

print(np.max(a1))
print(np.sum(a1))

print(np.max(a1,axis=0))
print(np.max(a1,axis=1))

# Mean/Median/Std dev/Var/log/exp/trigonometric operations

# DOT PRODUCT (m*n n*p   result = m*p)
a1=np.arange(12).reshape(3,4)
a3=np.arange(12,24).reshape(4,3)

print(np.dot(a1,a3))

# ROUND/CEIL
print(np.round(np.random.random((2,3))*100))


