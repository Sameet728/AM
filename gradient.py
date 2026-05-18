# import numpy as np
# import matplotlib.pyplot as plt

# # Function
# def f(x):
#     return x**2

# # Derivative
# def grad(x):
#     return 2*x

# # Initial value
# x = 8

# # Learning rate
# lr = 0.1

# # Number of iterations
# iterations = 20

# # Store values
# x_history = []
# y_history = []

# print("Iteration\tX value\t\tf(x)")

# for i in range(iterations):

#     x_history.append(x)
#     y_history.append(f(x))

#     print(i+1, "\t\t", round(x,4), "\t\t", round(f(x),4))

#     # Gradient Descent Update
#     x = x - lr * grad(x)

# # Graph
# x_vals = np.linspace(-10, 10, 200)
# y_vals = f(x_vals)

# plt.plot(x_vals, y_vals, label="f(x)=x^2")

# plt.scatter(x_history, y_history)

# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("Gradient Descent")

# plt.legend()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def grad(x):
    return 2*x

iteration =20
x=8
lr=0.1

xhistory=[];
yhistory=[];

for i in range(iteration):
    xhistory.append(x)
    yhistory.append(f(x))
    print("X value is : ",x, "and Y value is : ",f(x))
    x=x-lr*grad(x)

xvals=np.linspace(-10,10,200);
yvals=f(xvals);


plt.scatter(xhistory,yhistory);
plt.plot(xvals,yvals);
plt.show();