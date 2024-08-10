class Solution {
public:
    int maxPower(string s) {
        int n = s.size();
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
                curr_length = 1;
        }
        return max(curr_length, max_length);
    }
};