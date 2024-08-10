class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        int first = 0, last = n-1, k = n-1;
        vector<int> new_arr(n);
        while(first <= last){
            if(abs(nums[first]) < abs(nums[last])){
                int val = nums[last] * nums[last];
                new_arr[k] = val;
                last--;
                k--;
            }else{
                int val = nums[first] * nums[first];
                new_arr[k] = val;
                first++;
                k--;
            }
        }
        return new_arr;
    }
};