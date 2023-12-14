# %%
import matplotlib.pyplot as plt
# import numpy as np
day= [1,2,3,4,5,6,7]
no = [2,4,2,6,3,6,8]
colors=[10,40,46,25,64,35,50]
sizes=[100,150,251,548,510,210,260]
plt.scatter(day,no,c=colors,s=sizes,edgecolor="r",alpha=0.95)
plt.colorbar()
plt.title("SCATTER PLOT")
plt.xlabel("Day",fontsize=18)
plt.ylabel("No",fontsize=18)

plt.show()


# %%
import numpy as np
import random
x=np.arange(10,54)
plt.hist(x,edgecolor="y",bottom=10,orientation="horizontal",rwidth=0.65)
plt.title("HISTOGRAM")
plt.xlabel("Python")
plt.ylabel("no")
plt.show()


# %%
#pie chart plot
x=[10,20,30,40]
y=['c','c++','java','python']
ex=[0.2,0.0,0.0,0.0]
c=["r","g","b","y"]
plt.pie(x, labels=y, explode=ex, autopct="%0.1f%%", shadow=True, radius=1, labeldistance=1.1, startangle=0
,textprops={"fontsize":15}, counterclock=False, wedgeprops={"linewidth":5}, rotatelabels=False)

plt.title("pie chart")
plt.legend(loc=2)
plt.show()

# %%
#STEM PLOT
x = [1,2,3,4,5]
y = [2,5,3,7,9]
plt.stem(x,y,linefmt=":",label="PIE CHART",markerfmt="r+",bottom=1,orientation="vertical",basefmt="y")
plt.legend()
plt.show()

# %%
#step PLOT
x= [1,2,3,4,5,6,7,8]
y= [2,5,3,7,4,9,4,35]
plt.step(x,y,label="STACK PLOT",color="r",marker="o",markersize=8)
plt.legend()
plt.title("stackker")
plt.show()

# %%
#stack plot
x= [1,2,3,4,5,6,7,8]
y= [2,5,3,7,4,9,4,35]
plt.plot(x,y,label="STACK PLOT",color="r",marker="o",markersize=8)
plt.legend()
plt.title("stackker")
plt.show()

# %%
#fill betwen
x= [1,2,3,4,5,6]
y =[2,5,2,5,2,5]

plt.fill(x,y,color="y")
plt.show()

# %%
