class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        int breakPoint = -1;
        for (int i = len - 2; i >= 0 ; i--){
            if(nums[i] < nums[i+1]){
                breakPoint = i;
                break;
            }
        }
        if(breakPoint == -1){
            reverse(nums.begin(), nums.end());
            return;
        }
        for(int i = len - 1; i >= breakPoint; i--){
            if (nums[i] > nums[breakPoint])
            {
                swap(nums[i], nums[breakPoint]);
                break;
            }
        }
        reverse(nums.begin() + breakPoint + 1, nums.end());
        return;
    }
};