# 函数闭包

def f(x):
    result = x * 2
    
    def inner():
        print(result)
    return inner


fun1 = f(1)
fun1()