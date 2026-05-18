#%%
import numpy as np
import matplotlib.pyplot as plt

x = 10
learning_rate = 0.1
iterations = 20

for i in range(iterations):

    gradient = 2*x
    x = x-learning_rate*gradient

    print("Iterations",i+1,"x=",x)

print("Minimum value at:",x)

# %%
import numpy as np
from scipy.stats import norm

n     = 200
x_bar = 3.2   # sample mean
mu0   = 3     # population mean under H0
sigma = 0.8   # known std
alpha = 0.05


z=(x_bar-mu0)/(sigma/np.sqrt(n));
critical_v=norm.ppf(1-alpha/2);
print("Z value is : ",z);
print("Critical value is : ",critical_v);


if abs(z)>critical_v:
    print("Reject H0")
else:
    print("Fail to reject H0")

    
# %%
import numpy as np
from scipy.stats import t

# Given data
n = 15
x_bar = 24
mu0 = 20
s = 5
alpha = 0.05

# t-statistic
t_stat = (x_bar - mu0) / (s / np.sqrt(n))

# Degrees of freedom
df = n - 1

# Critical value (right-tailed)
t_critical = t.ppf(1 - alpha, df)



print("t statistic :", t_stat)
print("Critical t  :", t_critical)

# Decision
if t_stat > t_critical:
    print("Reject H0 – Training improved performance")
else:
    print("Fail to Reject H0 – No significant improvement")