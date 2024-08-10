class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum = 0;
        int overallMax = INT_MIN;
        int len = nums.size();
        for (int i = 0; i < len; i++){
            if(nums[i] + currSum > nums[i]){
                currSum += nums[i];
            }else{
                currSum = nums[i];
            }
            if(currSum > overallMax){
                overallMax = currSum;
            }
        }
        return overallMax;
    }
};