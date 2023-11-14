# %%
import numpy as np

array_1d = np.array([-10, -2, 0, 2, 17, 106,200])
print('The value at index 0:', array_1d[0])
#-ve index
print('The value at index -2: ', array_1d[-2])

print('Our original array is: ', array_1d)
print('Selected slice of the array is: ', array_1d[0:3])

print('Value in array_1d upto index 2 : ',array_1d[:2])
print('Value in array_1d from index 2 : ',array_1d[2:])

# %%
import numpy as np
arr = np.array([-84,23,93,383,2,323,-58])
print(arr)
arr[0] = 12
print(arr[0:5])

# %%
import numpy as np
ar_2d = np.arange(24)
# ar_sh2 = ar_2d.shape(6,4)
ar_2d.shape = (6,4)
print(ar_2d)

# %%
#or we can get a particular row means like this
print(ar_2d[4])
print(ar_2d[-2])
# print(/

print(arr_2d[:2,:2])