#include <iostream>
#include <algorithm>

int main()
{
    int r,b;
    std::cin >> r >> b;
    std::cout << std::min(r,b) << " " << std::max(((r-std::min(r,b))/2),((b-std::min(r,b))/2));
}