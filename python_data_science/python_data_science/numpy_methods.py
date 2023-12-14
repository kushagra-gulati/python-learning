# %%
import numpy as np
a= [1,2,3,4,5,6]
y = np.array(a)
print(y)
print(type(y))
print(y.ndim)

# %%
l = []
for i in range(1,5):
    int_1 = int(input("enter number: "))
    l.append(int_1)

print(np.array(l))
    

# %%
import numpy as np
l = [[1,2,3],[4,5,6],[7,8,9]]
# print(l)
matrix_new = np.array(l)
print(matrix_new)
print(matrix_new.ndim)

# %%
import numpy as np
list2 = np.array([[[1,2,3],[1,5,7],[6,4,9]]])
print(list2.ndim)

# %%
#arrange
import numpy as np
print(np.arange(1,20,2))
#end

# %%
#arange with dtype
import numpy as np
print(np.arange(1,20,3, dtype=float))
print(ll)

# %%
#zeroes method
import numpy as np
print(np.zeros(3))
print(np.zeros((4,6)) )

# %%
#eye method
print(np.eye(8))

# %%
#rand method
import numpy as np
print(np.random.rand(4))

# %%
#randint()
import numpy as np
print(np.random.randint(1,100))
print(np.random.randint(1,100,29))

# %%
#using arnge and randint()
import numpy as np
ar_ar = np.arange(16)
ar_rint = np.random.randint(0,100,10)
zer = np.eye(6)
print(zer)
print(ar_ar)
print(ar_rint)

# %%
#reshape
print(ar_ar.reshape(4,4))

# %%
#min and max()
import numpy as np
print(ar_ar.min())
print(ar_ar.max())

# %%
#argmax and argmin()
import numpy as np
arg = np.arange(16)
arg_1 = np.random.randint(0,100,10)

print(arg.min())
print(arg.argmax())
print(arg.argmin())


# %%
#size,shape and type of array
print(arg.shape)
print(arg.dtype)
print(arg.size)