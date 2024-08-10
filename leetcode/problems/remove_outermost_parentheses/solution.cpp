class Solution {
public:
    string removeOuterParentheses(string s) {
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
};