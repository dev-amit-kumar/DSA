class Solution {
public:
    int find(int row, int col, int m, int n, vector<vector<int>> &dp){
        if(row == m-1 && col == n-1) return 1;
        if(row >= m || col >= n) return 0;
        if(dp[row][col] != -1) return dp[row][col];
        int choice1 = find(row+1, col, m, n, dp);
        int choice2 = find(row, col+1, m, n, dp);
        return dp[row][col] = choice1 + choice2;
    }

    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m+1,vector<int>(n+1,-1));
        return find(0,0, m, n, dp);
    }
};