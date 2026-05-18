#%%
import numpy as np
import matplotlib.pyplot as plt

coin=np.random.choice(['H','T'],1000)

heads=np.sum(coin=='H')
tails=np.sum(coin=='T')

print("Heads =",heads)
print("Tails =",tails)

print("Experimental P(Head) =",heads/1000)
print("Theoretical P(Head) =",0.5)

plt.hist(coin)
plt.show()

# %%

data = np.random.poisson(5,1000)

print(data[:20])

plt.hist(data)
plt.xlabel("Events")
plt.ylabel("Frequency")
plt.show()

# %%
