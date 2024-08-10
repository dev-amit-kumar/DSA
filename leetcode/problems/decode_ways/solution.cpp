class Solution {
public:
    int find(string s, int i, vector<int> &dp){
        if (i == s.size()) return 1;
        if (s[i] == '0') return 0;
        if (dp[i] != -1) return dp[i];
        int not_take = find(s, i+1, dp);
        int take = 0;
        if(i < s.size() - 1 && (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6'))) 
            take = find(s, i + 2, dp);
        return dp[i] = take + not_take;
    }
    int numDecodings(string s) {
        vector<int> dp(s.size() + 1, -1);
        if(s.empty() || s[0] == '0')
            return 0;
        return find(s, 0, dp);
    }
};