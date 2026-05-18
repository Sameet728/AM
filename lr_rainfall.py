import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Rainfall data (X)
X = np.array([10, 20, 30, 40, 50]).reshape(-1,1)

# Water level data (Y)
Y = np.array([15, 25, 35, 45, 55])


model=LinearRegression();
model.fit(X,Y);
b0=model.intercept_;
b1=model.coef_[0];
eqn_y=model.predict(X);
print("The coefficients are :\n",b0,b1);

plt.scatter(X,Y);
plt.plot(X,eqn_y);
plt.xlabel("Rainfall (mm)"); plt.ylabel("Water Level (m)");
plt.title("Rainfall vs Water Level");
plt.show();