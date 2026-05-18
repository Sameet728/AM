import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = np.array([27, 20, 32, 25, 35, 22]).reshape(-1, 1)
Y = np.array([2600, 2100, 3050, 2550, 3390, 2250])
X = pd.DataFrame(X)

# # Model Fitting
# model = LinearRegression()
# model.fit(X, Y)
# beta_0 = model.intercept_
# beta_1 = model.coef_[0]
# print("Intercept (a):", beta_0)
# print("Slope (b)    :", beta_1)

# # Scatter Plot + Regression Line
# Y_pred = model.predict(X)
# plt.scatter(X, Y, label="Actual Data")
# plt.plot(X, Y_pred, label="Regression Line")
# plt.xlabel("Temperature (°C)"); plt.ylabel("Sales (₹)")
# plt.title("Regression Line with Scatter Plot")
# plt.legend(); plt.show()

# # Prediction at 30°C
# temp = np.array([[30]])
# predicted_sales = model.predict(temp)
# print("Predicted Sales at 30°C:", predicted_sales[0])

# # R² Score
# r2 = r2_score(Y, Y_pred)
# print("R-squared Score:", r2)


model=LinearRegression();
model.fit(X,Y);
b0=model.intercept_;
b1=model.coef_[0];
print("The coefficients are :\n",b0,b1);


yy=model.predict(X);
plt.scatter(X,Y);
plt.plot(X,yy);
plt.show();

r=r2_score(Y,yy)
print("R2 Score",r);