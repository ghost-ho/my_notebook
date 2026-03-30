import random

arr = [random.randint(0, 100) for _ in range(15)]
print(arr)

# 快速排序

left = 0
right = len(arr) - 1
basic_element = arr[left]

for i in range(len(arr)):
    if arr[right] < basic_element:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
    if arr[left] > basic_element:
        arr[left], arr[right] = arr[right], arr[left]
        right -= 1