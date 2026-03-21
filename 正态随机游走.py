import numpy as np
import matplotlib.pyplot as plt
from random import gauss

L = +1
R = -1

n = 100
points = [i for i in range(n)]
index = 0
values = [0 for i in range(n)]

while index < n - 1:
    if gauss(1, 3) < 0:
        values[index + 1] =values[index] - 1
    if gauss(0, 1) > 0:
        values[index + 1] = values[index] + 1
    index += 1

print(sum(values) / len(values))

plt.plot(points, values)
plt.show()
