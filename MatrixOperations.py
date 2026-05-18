# import numpy as np 

# a=np.array([[1,42,535,323],[5,43,22,43],[9,43,34,412],[434,5334,333,34]]);
# b=np.array([[3,5,3,2],[5,4,6,7],[8,9,4,5],[4,2,4,3]]);

# c=np.add(a,b);
# print("Addition of a and b is :\n",c);

# d=np.subtract(a,b);
# print("Subtraction of a and b is :\n",d);

# det_a=np.linalg.det(a);
# print("Determinant of a is :\n",det_a);

# inv_a=np.linalg.inv(a);
# print("Inverse of a is :\n",inv_a);


# en_value,en_vector=np.linalg.eig(a);
# print("Eigen values of a is :\n",en_value);
# print("Eigen vectors of a is :\n",en_vector);



import numpy as np 
a=np.array([[1,2342,343],[44,425,426],[567,68546,359]]);
b=np.array([[1,2,3],[4,5,6],[7,8,9]]);

c=np.add(a,b);
print("Addition of a and b is :\n",c);

d=np.subtract(a,b);
print("Subtraction of a and b is :\n",d);

e=np.multiply(a,b);
print("Multiplication of a and b is :\n",e);

f=np.dot(a,b);
print("Dot product of a and b is :\n",f);

g=np.cross(a,b);
print("Cross product of a and b is :\n",g);

h=np.linalg.det(a);
print("Determinant of a is :\n",h);

i=np.linalg.inv(a);
print("Inverse of a is :\n",i);

eigva,eigve=np.linalg.eig(a);
print("Eigen values of a is :\n",eigva);
print("Eigen Vectors of a is :\n",eigve);

