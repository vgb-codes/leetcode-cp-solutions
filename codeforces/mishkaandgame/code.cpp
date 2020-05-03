#include <iostream>

int main()
{
    int n, m = 0, f = 0;
    std::cin >> n;
    for(int i = 0; i < n; i++)
    {
        int a,b;
        std::cin >> a >> b;
        if(a > b)
        {
            m++;    
        }else if(a < b)
        {
            f++;
        }
    }

    if(m > f)
    {
        std::cout << "Mishka";
    }else if(m < f)
    {
        std::cout << "Chris";
    }else
    {
        std::cout << "Friendship is magic!^^";
    }
}