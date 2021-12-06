import numpy as np


arr1 = np.arange(10, 16)

print("1D The array is: ", arr1)
print("Shape of the array is : ", np.shape(arr1))

obj = 2
value = 40

arr = np.insert(arr1, obj, value, axis=None)
print("After inserting the new array is: ")
print(arr)
print("Shape of the new array is : ", np.shape(arr))



arr2= np.arange(16).reshape(4,4)
print("2D The array is: \n", arr2)
print("Shape of the array is : ", np.shape(arr2))

obj2 = 0
value2 = 40

arrr = np.insert(arr2, obj2, value, axis=None)
print("After inserting the new array is: ")
print(arrr)
print("Shape of the new array is : ", np.shape(arrr))