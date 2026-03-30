# 定义一个factorial函数来计算阶乘
def factorial(n):
    prefix = [1, 1]
    
    if n == 0 or n == 1:
        return prefix[n]
    else:
        for i in range(2, n + 1):
            prefix.append(prefix[i - 1] * i);
        return prefix[n]

n = int(input("请输入一个非负整数："))
s = 0

for i in range(1, n + 1):
    s += factorial(i)
print(f"阶乘求和结果为：{s}")