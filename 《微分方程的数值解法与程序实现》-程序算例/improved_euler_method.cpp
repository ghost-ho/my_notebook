#include <iostream>
#include <math.h>

static float f(float x, float y)
{
	return y - (2 * x / y);
}

int main()
{
	const int n = 50;

	float start, end;
	start = 0;
	end = 1;
	float h = (end - start) / (n - 1);
	float init_value = 1;

	float points[n] = { 0 };
	float values[n] = { 0 };
	values[0] = init_value;

	for (int i = 0; i < n; i++)
	{
		points[i] = start + i * h;
	}
	for (int i = 1; i < n; i++)
	{
		values[i] = values[i - 1] + h * f(points[i - 1], values[i - 1]);
	}

	for (int i = 0; i < n; i++)
	{
		std::cout << "(" << points[i] << ", " << values[i] << ")" << "\n";
	}

}