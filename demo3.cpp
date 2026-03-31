#include <iostream>
#include <vector>

static long long factorial(const int n)
{
	long long int prefix[n];
}
int main()
{
	int n, sum;
	sum = 0;
	std::cin >> n;
	for (int i = 1; i <= n; i++)
	{
		sum += factorial(i);
	}
	std::cout << sum;

}