import random

arr1 = [random.randint(0, 100) for _ in range(15)]
print(arr1)

for i in range(len(arr1)):
    for j in range(len(arr1) - i - 1):
        if arr1[j] >= arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]

print(arr1)