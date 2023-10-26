import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print("shallow copy will be :", arr)
print(x)
x= arr.copy()
arr[0] =33
print("deep copy will be as :",arr)
print(x)