# %%
import pandas as pd
import numpy as np
# print('numpy version :', np.__version__)
print('pandas version :', pd.__version__)


# %%
lab = ['X','Y','Z']
new_label = [.1,.2,.3]
data1 = [120,48,842]
print(pd.Series(data=data1))
print(pd.Series(data=lab))

# %%
#using numpy arrays
my_array = np.array(data1)
series = pd.Series(data=my_array,index=new_label)
print(series)


# %%
#using dictionaries
dict1= {"name": "kushagra", "age": 85,"city": "meerut"}
print(pd.Series(data=dict1))

dict2= {"name": "kushagra", "age": "85","city": "meerut"}
print(pd.Series(data=dict2))

# %%
#data fetching using pandas from series
dict3= {"name": "mukund", "age": 56,"city": "delhi"}
dict4= {"name": "mayank", "age": 26,"city": "kalka"}
ser1 = pd.Series(data=dict1)
ser2 = pd.Series(data=dict2)
ser3 = pd.Series(dict3)
ser4 = pd.Series(data=dict4)
# ser5 =ser1 + ser2
# print(ser5)
print("series1 will be: ",ser1.values)
print("series1 will be: ",ser2["age"])
print("series1 will be: ",ser3["city"])
print("series1 will be: ",ser4["name"],["age"])

# %%
