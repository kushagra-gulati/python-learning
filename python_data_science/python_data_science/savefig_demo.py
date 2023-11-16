# %%
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,2,5,8]

plt.plot(x,y,color="r")
plt.savefig("savefig demo.pdf",dpi=2000)
plt.show()