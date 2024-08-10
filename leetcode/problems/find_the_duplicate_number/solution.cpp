class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int temp = nums[0];
        for (int i = 1; i < n; i++){
            if(nums[i] == temp){
                return nums[i];
            }
            temp = nums[i];
        }
        return -1;
    }
};