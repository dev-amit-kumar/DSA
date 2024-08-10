class Solution {
public:
    int findLow(vector<int> nums, int target, int low, int high){
        int ans = -1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(nums[mid] == target){
                ans = mid;
                high = mid - 1;
            }
            else if (nums[mid] > target){
                high = mid -1;
            }
            else{
                low = mid + 1;
            }
        }
        return ans;
    }

    int findHigh(vector<int> nums, int target, int low, int high){
        int ans = -1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(nums[mid] == target){
                ans = mid;
                low = mid + 1;
            }
            else if (nums[mid] > target){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        return ans;
    }

    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int low = 0;
        int high = nums.size() - 1;
        vector<int> result;
        int lowValue = findLow(nums, target, low, high);
        if(lowValue == -1) return result;
        int highValue = findHigh(nums, target, low, high);
        for (int i = lowValue; i <= highValue; i++)
            result.push_back(i);
        return result;
    }
};