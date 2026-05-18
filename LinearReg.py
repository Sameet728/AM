import numpy as np;
import matplotlib.pyplot as plt;
from sklearn.metrics import r2_score;

x=np.array([1,2,3,4,5]);
y=np.array([2200,2800,3000,3500,4000]);

x_sq=x**2;
y_sum=np.sum(y);
x_sum=np.sum(x);
x_sq_sum=np.sum(x_sq);
x_y=x*y;
x_y_sum=np.sum(x_y);
n=len(x);

b1=(n*x_y_sum-x_sum*y_sum)/(n*x_sq_sum-x_sum**2);
b0=(y_sum-b1*x_sum)/n;

print("The coefficients are :\n",b0,b1);
print("The regression line is :\n",b0,"+",b1,"*x");

eqn_y=b1*x+b0;
plt.scatter(x,y);
plt.plot(x,eqn_y);
plt.show();


r=r2_score(y,eqn_y);
print("R2 Score",r);