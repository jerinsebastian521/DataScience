import numpy as np
array = np.arange(16).reshape(4,4)
print(array)
print("excluding the first row",array[0:])
print("excluding the last column",array[:-1])
print("elements of 1 st and 2 nd column in 2 nd and 3 rd row",array[0:1,1:2])
print("Display the elements of 2 nd and 3 rd column",array[:,[1,2]])
print("second & third element of first row",array[0:1, 1:3])
print("Display the elements from indices 4 to 10 in descending order")
