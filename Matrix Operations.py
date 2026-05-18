#%%
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[6,7]])

print ("Matrix A : ")
print(A)

print("Matrix B : ")
print(B)

#Addition
print("Addition")
print(A+B)

#Multiplication
print("Multiplication")
print(np.dot(A,B))

#Determinant
print("Determinant")
print(np.linalg.det(A))

#Inverse
print("Inverse")
print(np.linalg.inv(A))

#Eigenvaluse and Eigenvectors
values,vectors = np.linalg.eig(A)
print("Eigenvalues : ")
print(values)
print("Eigenvectors : ")
print(vectors)
# %%
