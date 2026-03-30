condition = lambda n: n % 2 == 0
num = 10
for i in range(num + 1):
	if condition(i):
		print(f"{i}是偶数")
	else:
		print(f"{i}是奇数")