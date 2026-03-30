def phi(g):
	def f(x):
		return x + g
	return f

# 再次抽象
# 考虑一个群元素g，我们可以通过一个映射phi把g变成映射phi(g)，
# 然后代入取值phi(g)(x)就得到一个具体的取值
# 那么就可以引入更高层的抽象：考虑两个群G,K之间的同态psi
# 然后定义
def psi(g):
	return g + 1
phi(1)