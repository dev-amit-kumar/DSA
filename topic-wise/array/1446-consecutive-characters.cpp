// Link: https://leetcode.com/problems/consecutive-characters/

#include <iostream>
#include <string>
using namespace std;

int find(string s, int n)
{
    int curr_length = 1;
    int max_length = 1;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == s[i + 1])
        {
            curr_length++;
            max_length = max(curr_length, max_length);
        }
        else
        {
            curr_length = 1;
        }
    }
    return max(curr_length, max_length);
}

int main()
{
    string s = "abbcccddddeeeeedcba";
    int n = s.size();
    int result = find(s, n);
    cout << result << endl;
}