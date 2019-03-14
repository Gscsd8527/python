import pandas as pd
import numpy as np
import matplotlib as plt
s1 = [6,7,8,5,9,6,4,2,3,5,8,6,7,9,7,2]
avg = np.mean(s1)
print(avg)
y1 = [i for i in range(len(s1))]
xdata = np.linspace(0,len(s1))
ydata = [avg for i in range(len(s1))]
plt.figure()
plt.plot(xdata,ydata,'r')
plt.plot(x1,y1,'bo')
plt.show()