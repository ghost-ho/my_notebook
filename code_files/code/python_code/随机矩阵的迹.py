import numpy as np
from random import randint

N = 100
nums = [i for i in range(1, N+1)]
A_trace = []

for i in nums:
    A = [
        [randint(0, 1) for i in [0, 1, 2, 3]],
        [randint(0, 1) for i in [0, 1, 2, 3]],
        [randint(0, 1) for i in [0, 1, 2, 3]],
        [randint(0, 1) for i in [0, 1, 2, 3]],
    ]
    A_trace.append(np.linalg.trace(A))

A_trace_average = 0
n = len(A_trace)
for i in A_trace:
    A_trace_average += i / n

A_trace_average_theory = len(A[0]) * 0.5

print(f"随机矩阵A的迹的期望值为{A_trace_average}.")
print(f"和理论值的差距为{A_trace_average - A_trace_average_theory}.")