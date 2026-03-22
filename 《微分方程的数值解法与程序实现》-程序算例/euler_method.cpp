#include <iostream>
#include <math.h>

static float f(float x, float y)
{
	return y - (2 * x / y);
}

void main1()
{
	// 给区间分段，插入的分点数量为n
	const int n = 10;
	// 区间起点和终点
	float start, end;
	start = 0;
	end = 1;
	// 步长
	float h = (end - start) / (n - 1);

	// 生成点列
	float points[n] = { 0 };
	float values[n] = { 0 };
	int index = 1;
	float init_value = 1;
	for (int i = 0; i < n; i++)
	{
		// 这一步是生成点列
		points[i] = start + i * h;
	}
	// 设置初值
	values[0] = init_value;
	// 迭代计算其他值
	while (index < n)
	{
		values[index] = values[index - 1] + h * f(points[index - 1], values[index - 1]);
		index += 1;
	}

	for (int i = 0; i < n; i++)
	{
		std::cout << "(" << points[i] << "," << values[i] << ")" << "\n";
	}
}