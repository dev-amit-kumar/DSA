class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<int> dp(amount+1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i<=amount; i++){
            for (int j = 0 ; j < n; j++){
                int sub = i - coins[j];
                if( i >= coins[j] && dp[sub] != INT_MAX){
                    dp[i] = min(dp[i], (dp[sub] + 1));
                }
            }
        }
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};