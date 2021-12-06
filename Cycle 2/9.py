import numpy as np



print("1D \n")
b = np.arange(5)
print(b)
y=np.diag(b, k=0)
print("diagonal \n",y)


print("2D \n")
a = np.arange(16).reshape((4,4))
print(a)
x=np.diag(a, k=0)
print("diagonal \n",x)

