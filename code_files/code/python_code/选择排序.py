import random

arr = [random.randint(0, 100) for _ in range(25)]
print(arr)

# 选择排序
for i in range(len(arr) - 1):
    # 默认arr[i]为最小
    min_element_index = i
    # 取之后的每一个元素arr[j]和min_element作比较
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_element_index]:
            # 更换新的最小元素
            min_element_index = j
    arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

print(arr)