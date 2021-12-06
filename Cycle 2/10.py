import numpy as np

print("1D \n")
a = np.arange(5)
print(a)
newar = np.append(a, 88)
print("after append\n",newar)


print("2D \n")
b=np.arange(4).reshape(2,2)
print(b)
newarr = np.append(b, [22, 23])
print("after append\n",newarr.reshape(3,2))