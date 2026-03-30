a, b, c, f = int(input()), int(input()), input(), int(input())
# a, b分别代表高度和宽度
# c是一个可见字符
# f是一个布尔值, f=0代表空心, f=1代表实心

if f == 1:
    for i in range(a):
        for j in range(b):
            print(c, end='')
        print()
elif f != 1:
    for i in range(a):
        if i == 0 or i == a - 1:
            for j in range(b):
                print(c, end='')
            print()
        else:
            print(c, end='')
            for j in range(1, b - 1):
                print(' ', end='')
            print(c)