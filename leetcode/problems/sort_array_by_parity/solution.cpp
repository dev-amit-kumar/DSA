class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while(left < right){
            if(nums[left] % 2 == 0)
                left++;
            else if (nums[right] % 2 == 1)
                right--;
            else if(nums[left] % 2 == 1 && nums[right] % 2 == 0){
                swap(nums[left], nums[right]);
                left++;
                right--;
            }
        }
        return nums;
    }
};