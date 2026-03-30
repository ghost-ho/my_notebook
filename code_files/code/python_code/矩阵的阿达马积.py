import random

arr1 = [random.randint(0, 100) for _ in range(15)]
arr2 = [random.randint(0, 100) for _ in range(15)]

arr_multi = [0 for _ in range(15)]

for j in range(15):
    arr_multi[j] = arr1[j] * arr2[j]

print(arr1, f"  长度为{len(arr1)}")
print(arr2, f"  长度为{len(arr2)}")
print(arr_multi, f"  长度为{len(arr_multi)}")