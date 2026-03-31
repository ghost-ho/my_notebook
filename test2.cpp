//#include <iostream>
//
//int main()
//{
//	int h;
//	std::cin >> h;
//	double h_sum, h_end;
//	h_sum = h;
//	h_end = h / 64;
//	double result = 1;
//	for (int i = 0; i < 9; i++)
//	{
//		for (int j = 0; j < i; j++)
//		{
//			result = result * 2;
//		}
//		h_sum += h_sum / result;
//	}
//	h_sum += h_end;
//	std::cout << h_sum << "\n";
//	std::cout << h_end;
//}