//#include <iostream>
//#include <vector>
//#include <iomanip>
//
//int main()
//{
//	int n, k;
//	std::cin >> n >> k;
//	std::vector<int> A, B;
//	for (int i = 1; i <= n; i++)
//	{
//		if (i % k == 0)
//		{
//			A.push_back(i);
//		}
//		else
//		{
//			B.push_back(i);
//		}
//	}
//
//	double a, b;
//	a = 0;
//	b = 0;
//	for (int i = 0; i < A.size(); i++)
//	{
//		a += A[i];
//	}
//	for (int i = 0; i < B.size(); i++)
//	{
//		b += B[i];
//	}
//	a = a / A.size();
//	b = b / B.size();
//	std::cout << std::fixed << std::setprecision(1) << a << " " << b;
//
//}