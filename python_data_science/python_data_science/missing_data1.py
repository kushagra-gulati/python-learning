# %%
#missing data
import numpy as np
import pandas as pd

dict1 = {
    "A": [1, 2, np.nan, 45, np.nan],
    "B": [np.nan, np.nan, np.nan, np.nan, np.nan],
    "C": [223, 34, 13, 44, 2],
    "D": [203, np.nan, np.nan, 23, 5684],
}

df = pd.DataFrame(dict1)
print(df)



# %%
print(df.isnull())
print(df.notnull())

# %%
#doing sum checking
print(df['B'])
print(df.sum())

# %%
#hresh ans axis
print(df.dropna(axis=1))
print(df.dropna(axis=0))
print(df.dropna(thresh=1))

# %%
print(df.fillna(value="done"))

# %%
