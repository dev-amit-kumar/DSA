// Link: https://practice.geeksforgeeks.org/problems/outermost-parentheses/1

#include <iostream>
using namespace std;

string removeOuter(string &s)
{
    int n = s.length();
    string temp = "";
    string result = "";
    int open = 0;
    int close = 0;
    for (int i = 0; i < n; i++)
    {
        temp += s[i];
        if (s[i] == '(')
            open++;
        else
            close++;
        if (open == close)
        {
            result += temp.substr(1, temp.length() - 2);
            open = 0;
            close = 0;
            temp = "";
        }
    }
    return result;
}

int main()
{
    string s = "(()())(())";
    string result = removeOuter(s);
    cout << result << endl;
    return 0;
}