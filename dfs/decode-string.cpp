// https://leetcode.com/problems/decode-string/

#include <iostream>
#include <string>
#include <stack>
using namespace std;

void dfs(string &input, int i, stack<int> &numberTrack, stack<string> &strTrack)
{
    if (i == input.size())
        return;
    char c = input[i];
    if (c == ']')
    {
        string curr = "";
        string top = strTrack.top();
        while (top != "[")
        {
            strTrack.pop();
            curr = top + curr;
            top = strTrack.top();
        }
        strTrack.pop();
        int num = numberTrack.top();
        numberTrack.pop();
        string newCurr = "";
        for (int j = 0; j < num; j++)
            newCurr += curr;
        strTrack.push(newCurr);
        i++;
        return dfs(input, i, numberTrack, strTrack);
    }
    else if (isdigit(c))
    {
        int k = 0;
        k = k * 10 + input[i] - '0';
        if (i > 0 && isdigit(input[i - 1]))
        {
            k = numberTrack.top() * 10 + k;
            numberTrack.pop();
        }
        numberTrack.push(k);
        i++;
        return dfs(input, i, numberTrack, strTrack);
    }
    else
    {
        string eg;
        eg += c;
        strTrack.push(eg);
        i++;
        return dfs(input, i, numberTrack, strTrack);
    }
}

string decodeString(string input)
{
    stack<int> numberTrack;
    stack<string> strTrack;
    int i = 0;
    dfs(input, i, numberTrack, strTrack);
    string result = "";
    while (!strTrack.empty())
    {
        result = strTrack.top() + result;
        strTrack.pop();
    }
    return result;
}

int main()
{
    string input = "2[abc]3[cd]ef";
    string result = decodeString(input);
    cout << result << endl;
    return 0;
}