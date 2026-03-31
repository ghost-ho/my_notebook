#include <iostream>
#include <iomanip>

long long int factorial(int n)
{
	if (n == 0 || n == 1)
	{
		return 1;
	}
	else
	{
		return n * factorial(n - 1);
	}
}

int main()
{
	long long int sum = 0;
	int index = 1;
	while (index <= 30)
	{
		sum += factorial(index);
		index += 1;
	}
	std::cout << std::fixed << std::setprecision(3) << sum << "\n";
}