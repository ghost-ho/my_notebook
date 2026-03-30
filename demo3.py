import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y1 = np.sin(x) + x
y2 = np.cos(x) + x
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()