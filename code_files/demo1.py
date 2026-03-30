def f(x):
    def inner(y):
        return x + y
    return inner

print(f(1)(2))
print(f(2)(1))