#include <iostream>
#include <vector>

int main()
{
    std::vector<int> money;
    money.push_back(100);
    money.push_back(20);
    money.push_back(10);
    money.push_back(5);
    money.push_back(1);
    
    int n,count = 0;
    std::cin >> n;
    for(int i = 0; i < money.size(); i++)
    {
        count += n/money[i];
        n %= money[i];
    }
    std::cout << count;
}