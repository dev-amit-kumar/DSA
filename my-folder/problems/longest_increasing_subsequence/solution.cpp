class Solution {
public:
    int find(vector<int>& nums, vector<vector<int>>& dp, int idx, int prev){
        if(idx == nums.size()){
            return 0;
        }
        if(dp[idx][prev+1] != -1){
            return dp[idx][prev+1];
        }
        int not_take = 0 + find(nums, dp, idx+1, prev);
        int take = 0;
        if(prev == -1 || nums[idx] > nums[prev]){
            take = 1 + find(nums, dp, idx+1, idx);
        }
        return dp[idx][prev+1] = max(not_take, take);
    }
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n + 1, -1));
        return find(nums, dp, 0, -1); 
    }
};