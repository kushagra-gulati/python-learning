# %%
import numpy as np
import pandas as pd
df1 = pd.DataFrame({'key':['a','b','c','d','e'],'A1': range(5), 'B1':range(5,10)})
df2 = pd.DataFrame({'key': ['a', 'b', 'c'], 'A2': range(3), 'B2':range(3,6)})
print("Dataframe 1\n", df1)
print("Dataframe 2\n", df2)




# %%
MERGING

# %%
#practice merging
print(pd.merge(df1,df2,how = 'inner',on='key'))
print(pd.merge(df1,df2,how = 'outer',on='key'))
print(pd.merge(df1,df2,how = 'left',on='key'))
print(pd.merge(df1,df2,how = 'right',on='key'))

# %%
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', np.nan]},
                         index=[4,5,6,7])

print(pd.concat([df1,df2]))

# %%
# joining
b1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

b2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

print(b1.join(b2))
print(b2.join(b1))


# %%


# %%
