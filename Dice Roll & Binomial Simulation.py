#%%
import numpy as np
import matplotlib.pyplot as plt

rolls = np.random.randint(1,7,1000)

print("First 20 rolls : ")
print(rolls[:20])

for i in range(1,7):
    print("Count of",i,":",np.sum(rolls==i))

plt.hist(rolls,bins=6)
plt.xlabel("Dice Faces")
plt.ylabel("Frequency")
plt.show()

#%%

data = np.random.binomial(10,0.1,1000)

print(data[:20])

plt.hist(data)
plt.xlabel("Number of successes")
plt.ylabel("Frequency")
plt.show()


# %%
