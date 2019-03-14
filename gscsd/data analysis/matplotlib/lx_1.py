import numpy as np
from matplotlib import pyplot as plt

x = np.arange(11)
y = 2 * x + 5
plt.title('title')
plt.xlabel('X')
plt.ylabel('y')
plt.plot(x, y)
plt.show()
