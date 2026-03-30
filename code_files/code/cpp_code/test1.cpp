#include <iostream>

int main()
{
    int a, b, f;
    char c;
    std::cin >> a >> b >> c >> f;
    if (f != 0)
    {
        for (int i = 1; i <= a; i++)
        {
            for (int j = 1; j <= b; j++)
            {
                std::cout << c;
            }
            std::cout << "\n";
        }
    }
    else
    {
        for (int i = 1; i <= a; i++)
        {
            if (i == 1 || i == a)
            {
                for (int j = 1; j <= b; j++)
                {
                    std::cout << c;
                }
                std::cout << "\n";
            }
            else
            {
                std::cout << c;
                for (int k = 2; k < a; k++)
                {
                    std::cout << " ";
                }
                std::cout << c << "\n";
            }
        }
    }
}