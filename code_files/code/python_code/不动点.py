import numpy as np

x = 0.1
N = 25000
for i in range(N):
    x = np.sin(x)
print(x)