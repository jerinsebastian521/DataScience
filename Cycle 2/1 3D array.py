import numpy as np

x3 = np.arange(12) 
x=x3.reshape(3,4)

print(x)


convertedArray = x.astype(np.float32)
print(convertedArray)