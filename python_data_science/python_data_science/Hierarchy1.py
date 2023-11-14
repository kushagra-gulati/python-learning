# %%
import numpy as np
import pandas as pd
dict1= {"name": "kushagra", "age": 85,"city": "meerut"}
print(pd.Series(data=dict1))

dict2= {"name": "kushagra", "age": "85","city": "meerut"}
print(pd.Series(data=dict2))

# %%
#hierarchical indexing starts
se=np.random.seed(42)
print(se)

# %%
df = pd.DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=['AB','ON','BC'])
print(df)

# %%
print(df.loc['b'].loc[2]['BC'])
print(df.loc['a'].loc[1]['ON'])

# %%
print(df.index.names)

# %%
df.index.names = ['l1','l2']
print(df)

# %%
#xs method
print(df.xs('a'))
print(df.loc['a'])