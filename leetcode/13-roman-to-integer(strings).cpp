// Link: https://leetcode.com/problems/roman-to-integer/

#include <iostream>
#include <unordered_map>
using namespace std;

int romanToInt(string s)
{
    int total = 0;
    int n = s.length();
    int i = 0;
    while (i < n)
    {
        if (s[i] == 'I')
        {
            if (s[i + 1] == 'V')
            {
                total += 4;
                i++;
            }
            else if (s[i + 1] == 'X')
            {
                total += 9;
                i++;
            }
            else
                total += 1;
        }
        else if (s[i] == 'X')
        {
            if (s[i + 1] == 'L')
            {
                total += 40;
                i++;
            }
            else if (s[i + 1] == 'C')
            {
                total += 90;
                i++;
            }
            else
                total += 10;
        }
        else if (s[i] == 'C')
        {
            if (s[i + 1] == 'D')
            {
                total += 400;
                i++;
            }
            else if (s[i + 1] == 'M')
            {
                total += 900;
                i++;
            }
            else
                total += 100;
        }
        else if (s[i] == 'V')
            total += 5;
        else if (s[i] == 'L')
            total += 50;
        else if (s[i] == 'D')
            total += 500;
        else if (s[i] == 'M')
            total += 1000;
        i++;
    }
    return total;
}

int main()
{
    string s = "MCMXCIV";
    cout << romanToInt(s) << endl;
    return 0;
}