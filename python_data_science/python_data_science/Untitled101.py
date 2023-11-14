# %%
import pandas as pd
import numpy as np

ind = 'r1 r2 r3 r4 r5 r6 r7 r8 r9 r10'.split()
col =  'c1 c2 c3 c4 c5 c6 c7 c8 c8 c10'.split()
print(ind)

arr2d = np.arange(0,100)
print(arr2d)
reshap = arr2d.reshape(10,10)
print(reshap)

# %%
#using data+frame methods

dfe = pd.DataFrame(data=reshap,index=ind,columns =col)
print(dfe)

# %%
#fetching columns
print(dfe[["c1","c3"]])
#second approach method
print(dfe.c7)

# %%
dfe.drop(["c8"],axis =1,inplace= True)
print(dfe)

# %%
print(pd.DataFrame(data=reshap,index=ind,columns=col))

# %%
# dfe['c11'] = dfe['c9'] + dfe['c10']
# print(dfe)

# %%
print(dfe.loc[['r2','r3']])

# %%
print(dfe.iloc[[1,2]])
print("Subset \n",dfe.loc[['r1','r2'],['c1','c2']])