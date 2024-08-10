class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sumValue = 0;
        int n = nums.size();
        for (int i = 0; i < k; i++){
            sumValue += nums[i];
        }
        if(n == k) return sumValue / k;
        double curr = sumValue;
        for (int i = k; i < n; i++){
            curr = curr + nums[i] - nums[i-k];
            sumValue = max(sumValue, curr);
        }
        return sumValue / k;
    }
};