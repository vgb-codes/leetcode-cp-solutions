#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    std::string in;
    std::getline(std::cin >> std::ws,in);
    if(in.find('1') != std::string::npos)
    {
        std::cout << "HARD" << std::endl;
    }else{
        std::cout << "EASY" << std::endl;
    }
}