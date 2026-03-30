import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x, y):
    return y - 2 * x

# 节点数量
n = 15

# 起点和终点
start = 0.0
end = 2.0

# 步长
h = (end - start) / n

# 生成初始化点列
points = [start + i * h for i in range(n)]
values = [0 for _ in range(n)]

# 初值
init_value = 1
values[0] = init_value

index = 1
while index < n:
    values[index] = values[index - 1] + h * f(points[index - 1], values[index - 1])
    index += 1

plt.plot(points, values)
plt.show()