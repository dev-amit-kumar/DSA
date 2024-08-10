class Solution {
public:
    int find(int curr, vector<int>& nums, vector<int> & dp){
        if(curr >= nums.size()) return 0;
        if(dp[curr] != -1) return dp[curr];
        int take = nums[curr] + find(curr + 2, nums, dp);
        int not_take = 0 + find(curr + 1, nums, dp);
        return dp[curr] = max(take, not_take);
    }

    int rob(vector<int>& nums) {
        vector<int>dp(nums.size(), -1);
        int curr = 0;
        return find(curr, nums, dp);
    }
};