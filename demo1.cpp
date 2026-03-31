#include <iostream>

int main()
{
	// 打印矩形
	int width, height;
	bool b; // true代表实心; false代表空心
	char c;
	std::cin >> width >> height >> c >> b;

	if (b)
	{
		for (int i = 1; i <= height; i++)
		{
			for (int j = 1; j <= width; j++)
			{
				std::cout << c;
			}
			std::cout << "\n";
		}
	}
	else
	{
		for (int i = 1; i <= height; i++)
		{
			if (i == 1 || i == height)
			{
				for (int j = 1; j <= width; j++)
				{
					std::cout << c;
				}
				std::cout << "\n";
			}
			else
			{
				std::cout << c;
				for (int j = 2; j < width; j++)
				{
					std::cout << " ";
				}
				std::cout << c << "\n";
			}
		}
	}

}