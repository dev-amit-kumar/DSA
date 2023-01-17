class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        int m = strs[0].size();
        for (int i = 0; i < n; i++)
        {
            int j = 0;
            while (j < strs[i].length() && strs[i][j] == strs[0][j])
                j++;
            m = min(m, j);
        }
        return strs[0].substr(0, m);
    }
};