# %%
#axis demo
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[3,1,5,2]
plt.plot(x,y)
# plt.xticks(x)
# plt.yticks(y)

# plt.xlim(0,10)
# plt.ylim(0,22)

plt.axis([0,10,0,7])
plt.show()