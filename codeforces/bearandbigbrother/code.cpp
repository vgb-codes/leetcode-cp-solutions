#include <iostream>

int main()
{
    int l,b;
    int i = 0;
    std::cin >> l >> b;
    while(l<=b)
    {
        l*=3;
        b*=2;
        i++;
    }
    std::cout << i;
}