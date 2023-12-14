# %%
# import numpy as np
import pandas as pd


# %%
var = pd.DataFrame({"name": ["a","b","c","d","a","b","a","b","c","c","d"],
                     "Sub1": [12,13,48,45,25,13,29,52,19,25,35],
                     "Sub2": [26,45,29,21,22,23,24,29,27,28,37]})
var

# %%
var_new = var.groupby("name")
var_new

# %%
for x,y in var_new:
    print(x)
    print(y)
    print()

# %%
var_new.get_group("a")

# %%
var_new.get_group("b")

# %%
var_new.min()
# var_new.max()

# %%
var_new.mean()

# %%
li = list(var_new)
# li

# %%
var_new.describe()

# %%
