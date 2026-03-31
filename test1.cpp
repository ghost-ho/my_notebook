//#include <iostream>

//int main()
//{
//	int a, b, f;    // 行数、列数、是否空心(0->空心,1->实心)
//	char c;         // 字符
//
//	std::cin >> a >> b >> c >> f;
//
//	if (f != 0)
//	{
//		for (int i = 0; i < a; i++)
//		{
//			for (int j = 0; j < b; j++)
//			{
//				std::cout << c;
//			}
//			std::cout << "\n";
//		}
//	}
//	else
//	{
//		for (int i = 0; i < a; i++)
//		{
//			if (i == 0 || i == a - 1)
//			{
//				for (int j = 0; j < b; j++)
//				{
//					std::cout << c;
//				}
//			}
//			else
//			{
//				std::cout << c;
//				for (int j = 1; j < b - 1; j++)
//				{
//					std::cout << " ";
//				}
//				std::cout << c;
//			}
//			std::cout << "\n";
//		}
//	}
//}