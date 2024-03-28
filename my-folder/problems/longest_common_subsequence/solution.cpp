class Solution {
public:
    // int find(string text1, string text2, int ind1, int ind2, vector<vector<int>> &dp){
    //     if(ind1 < 0 || ind2 < 0) return 0;
    //     if(dp[ind1][ind2] != -1) return dp[ind1][ind2];
    //     if(text1[ind1] == text2[ind2])
    //         return dp[ind1][ind2] = 1 + find(text1, text2, ind1 - 1, ind2 - 1, dp);
    //     return dp[ind1][ind2] = max(find(text1, text2, ind1, ind2 - 1, dp), find(text1, text2, ind1 - 1, ind2, dp));
    // }

    int find(string s1, string s2){
        vector<vector<int>>dp(s1.size()+1,vector<int>(s2.size()+1,0));
        // for i==0
        for(int j=0;j<=s2.size();j++){
            dp[0][j] = 0;
        }
        // for j==0
        for(int i=0;i<=s1.size();i++){
            dp[i][0] = 0;
        }
        for(int i=1;i<=s1.size();i++){
            for(int j=1;j<=s2.size();j++){
                if(s1[i-1] == s2[j-1]){
                    dp[i][j] = 1 + dp[i-1][j-1];
                }
                else{
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[s1.size()][s2.size()];
    }

    int longestCommonSubsequence(string text1, string text2) {
        // int n = text1.size();
        // int m = text2.size();
        // vector<vector<int>> dp(n, vector<int>(m, -1));
        // return find(text1, text2, n-1, m-1, dp);
        return find(text1, text2);
    }
};