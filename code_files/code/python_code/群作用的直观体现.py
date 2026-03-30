# 群作用

# 模3加法
# def add3(a, b):
#     return (a + b) % 3

# 那我们可以用函数闭包得到模n加法
# 具体来说，是每一个模数mod都映射到对应的模运算加法
def addn(mod):
    def add_mod(a, b):
        return (a + b) % mod
    return add_mod

c = addn(5)(2, 3)
print(c)