class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++)
        {
            int temp = target - nums[i];
            if (mp.find(temp) == mp.end()) // element not found
                mp[nums[i]] = i;
            else // element found
                return {mp[temp], i};
        }
        return {-1, -1};
    }
};