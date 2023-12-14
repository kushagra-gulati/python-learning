# %%
import numpy as np
import pandas as pd
ata_dict = {'col_1':[1,2,3,4,5],
           'col_2':[111,222,333,111,555],
           'col_3':['alpha','bravo','charlie',np.nan,np.nan]}
ata_dict

# %%
df = pd.DataFrame(ata_dict,index=[1,2,3,4,5])
df

# %%
df.info()

# %%
df.head(2)

# %%
df.isnull()

# %%
df.dropna(axis=0)

# %%
df.dropna(axis=1)

# %%
df.fillna("insertion")

# %%
df.fillna(value='abc')

# %%
df.nunique()

# %%
df.value_counts()

# %%
df.sort_values(by='col_3',inplace=False)

# %%
