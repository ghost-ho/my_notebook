import numpy as np
from random import randint

N = 100
n = 1
nums = [i for i in range(1, N+1)]
A_det = []

for i in nums:
    A = [
        [randint(0, n) for i in [0, 1, 2, 3]],
        [randint(0, n) for i in [0, 1, 2, 3]],
        [randint(0, n) for i in [0, 1, 2, 3]],
        [randint(0, n) for i in [0, 1, 2, 3]],
    ]
    A_det.append(np.linalg.det(A))

A_det_average = 0
n = len(A_det)
for i in A_det:
    A_det_average += i / n

# A_det_average_theory = len(A[0]) * 0.5

print(f"随机矩阵A的行列式的期望值为{A_det_average}.")
# print(f"和理论值的差距为{A_det_average - A_det_average_theory}.")