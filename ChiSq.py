#%%
import numpy as np
from scipy.stats import chi2_contingency

data = np.array([
    [30,20],
    [25,35]
])

chi,p,dof,expected = chi2_contingency(data)

print ("Chi-square value : ",chi)
print("Degree of freedom : ",dof)
print("P-value : ",p)
print(expected)

if p < 0.05:
    print("Reject H0")
    print("Variables are dependent")
else:
    print("Fail to Reject H0")
    print("Variables are independent")

