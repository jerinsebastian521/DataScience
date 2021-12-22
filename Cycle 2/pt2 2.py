import numpy as np

a=np.arange(4).reshape(2,2)
print(a)

print("* \n",a*a*a)

print("cube of each element of the matrix power()\n",np.power(a, 3))

b=a*a
print("cube of each element of the matrix multiply\n",np.multiply(a,b))


c = np.identity(2, dtype = float)
print("Identity Matrix : \n", c)

x=np.arange(16).reshape(4,4)
y=np.arange(16).reshape(4,4)
print("x2+2y\n",x*x+2*y)


