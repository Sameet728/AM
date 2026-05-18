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



print("t statistic :", round(t_stat, 4))
print("Critical t  :", round(t_critical, 4))

# Decision
if t_stat > t_critical:
    print("Reject H0 – Training improved performance")
else:
    print("Fail to Reject H0 – No significant improvement")