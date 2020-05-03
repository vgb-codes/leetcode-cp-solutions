#include <iostream>
#include <map>

int main()
{
    std::map<std::string,int> poly;
    poly["Tetrahedron"] = 4;
    poly["Cube"] = 6;
    poly["Octahedron"] = 8;
    poly["Dodecahedron"] = 12;
    poly["Icosahedron"] = 20;
    int n, res = 0;
    std::cin >> n;

    for(int i = 0; i < n; i++)
    {
        std::string s;
        std::cin >> s;
        res += poly[s];
    }

    std::cout << res;
}   