# %%
import numpy as np

var1 = np.array([1,2,3])
print(var1)

var2 = np.array([[1],[2],[3]])
print(var2.shape)

print(var1 + var2)

# %%
x = np.array([[1],[2]])
print(x.shape)
y =np.array([[1,2,3],[1,2,3]])
print(x+y)

# %%

arr = np.arange(0,10)
print(arr)
arr[0:5] = 500
print(arr)

# %%
#on 2d array
array2 = np.ones((4,4))
print(array2)
array2[-4]= 300# or [0] acc to indexing from positive to negative or reverse
print(array2)

# %%
print(array2 + np.arange(0,4))