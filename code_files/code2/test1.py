import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * y

start, end, N = 0.0, 1.0, 1000
h = (end - start) / (N - 1)
x = [i for i in range(N)]
y = [0 for i in range(N)]
init_value = 1.0
y[0] = init_value

for i in range(N):
    y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])

plt.plot(x, y)
plt.show()