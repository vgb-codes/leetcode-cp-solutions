#include <iostream>
#include <string>

int main()
{
    int n;
    std::cin >> n;
    std::string out;
    for (int i = 1; i <= n; i++)
    {
        if(i % 2 != 0)
        {
            out.append("I hate ");
        }else{
            out.append("I love ");
        }
        if(i != n)
        {
            out.append("that ");
        }else
        {
            continue;
        }
    }
    out.append("it");
    std::cout << out;
}