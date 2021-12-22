import numpy as np
a= np.random.randint(5,size=(4,4))
print(a)

inv=np.linalg.inv(a)
print("inverse\n",inv)

rank = np.linalg.matrix_rank(a)
print("Rank of the given Matrix is : ",rank)

det=np.linalg.det(a)
print("determinant:",det)

arr=a.flatten()
print("transform matrix into 1D array",arr)

w, v = np.linalg.eig(a)
print("Printing the Eigen values of the given square array:\n",w)
print("Printing Right eigenvectors of the given square array:\n",v)  