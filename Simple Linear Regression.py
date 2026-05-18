#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = {
    "Orders": [10,20,30,40,50,60,70,80,90,100],
    "Revenue": [1000,9800,2600,3400,400,5000,5800,6600,1400,8200]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("data.csv created")

#%%
#Read Dataset
df = pd.read_csv("data.csv")

x = df[['Orders']]
y = df[['Revenue']]

model = LinearRegression()

model.fit(x,y)

pred = model.predict(x)

print("Slope:",model.coef_)
print("Intercept:",model.intercept_)

plt.scatter(x,y)
plt.plot(x,pred)
plt.xlabel("Orders")
plt.ylabel("Revenue")
plt.show()


