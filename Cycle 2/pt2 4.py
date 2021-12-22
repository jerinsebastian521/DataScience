import numpy as np

a=np.arange(4).reshape(2,2) 
b=np.arange(4).reshape(2,2) 
c=np.arange(4).reshape(2,2) 
print(a)
print(b)
print(c)
d=np.matmul(a,b)
x=np.matmul(d,c)
print(x)
