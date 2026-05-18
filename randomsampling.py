import pandas as pd
import numpy as np

# Create Hospital Dataset

np.random.seed(10)

data = {
    "Patient_ID": range(1, 21),

    "Department": [
        "ICU","ICU","ICU","ICU","ICU",
        "OPD","OPD","OPD","OPD","OPD",
        "Emergency","Emergency","Emergency",
        "Emergency","Emergency",
        "General","General","General",
        "General","General"
    ],

    "Waiting_Time": np.random.randint(5, 60, 20)
}

# Create DataFrame
df = pd.DataFrame(data)

print("----- ORIGINAL DATASET -----")
print(df)

# ---------------- RANDOM SAMPLING ----------------

random_sample = df.sample(n=5)

print("\n----- RANDOM SAMPLE -----")
print(random_sample)

# ---------------- STRATIFIED SAMPLING ----------------

# Select 2 samples from each department
stratified_sample = df.groupby("Department").sample(2)


ans=df.groupby("Department").sample(2);

print("\n----- STRATIFIED SAMPLE -----")
print(ans)