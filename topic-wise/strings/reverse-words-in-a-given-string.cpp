// Link: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1

#include <iostream>
using namespace std;

string reverseWords(string &s)
{
    int n = s.length();
    string temp = "";
    string result = "";
    for (int i = 0; i < n; i++)
    {
        if (s[i] == ' ')
        {
            result = temp + ' ' + result;
            temp = "";
        }
        else
        {
            temp += s[i];
        }
    }
    result = temp + ' ' + result;
    result.pop_back();

    while (result[0] == ' ' || result[result.length() - 1] == ' ')
    {
        if (result[0] == ' ')
            result.erase(0, 1);
        if (result[result.length() - 1] == ' ')
            result.pop_back();
    }
    return result;
}

int main()
{
    string s = "    i like this program very much    ";
    string result = reverseWords(s);
    cout << result << endl;
    return 0;
}