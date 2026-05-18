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
    print("Fail to reject H0");