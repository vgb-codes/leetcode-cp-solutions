#include <iostream>
#include <algorithm>

int main()
{
    int n;
    std::string in;
    std::cin >> n;
    std::getline(std::cin >> std::ws,in);
    int a = std::count(in.begin(), in.end(), 'A');
    int d = std::count(in.begin(), in.end(), 'D');
    if(a > d)
    {
        std::cout << "Anton";
    }else if (a < d)
    {
        std::cout << "Danik";
    }else
    {
        std::cout << "Friendship";
    }
}