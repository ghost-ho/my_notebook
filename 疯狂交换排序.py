import random

arr1 = [random.randint(0, 100) for _ in range(5)]
print(arr1)

# 疯狂交换来排序
for i in range(len(arr1) - 1):
    for j in range(i+1, len(arr1)):
        if arr1[j] <= arr1[i]:
            arr1[i], arr1[j] = arr1[j], arr1[i]
        print(arr1)
