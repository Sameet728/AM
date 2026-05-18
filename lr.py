import numpy as np
import matplotlib.pyplot as plt


x=np.array([27,20,32,25,35,22])
y=np.array([2600,2100,3050,2550,3390,2250])

n=len(x);
x_sq=x**2;
x_sum=np.sum(x)
y_sum=np.sum(y)
xy_sum=np.sum(x*y)
sum_x_sq=np.sum(x_sq)

b1=(n*xy_sum-x_sum*y_sum)/(n*sum_x_sq-x_sum**2)
b0=(y_sum-b1*x_sum)/n

y_pred=b0+b1*x

ans=b0+b1*30;
print("The coefficients are :\n",b0,b1);
print("Predicted sales at 30°C:",ans);



plt.scatter(x,y)
plt.plot(x,y_pred)
plt.show()