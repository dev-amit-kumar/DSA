class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        int mid;
        int lower_bound = -1;
        int upper_bound = -1;
        vector<int> result;
        while (start <= end)
        {
            mid = (start + end) / 2;
            if (nums[mid] == target)
            {
                end = mid - 1;
                lower_bound = mid;
            }
            else if (target < nums[mid])
                end = mid - 1;
            else
                start = mid + 1;
        }
        start = 0;
        end = nums.size() - 1;
        while (start <= end)
        {
            mid = (start + end) / 2;
            if (nums[mid] == target)
            {
                start = mid + 1;
                upper_bound = mid;
            }
            else if (target < nums[mid])
                end = mid - 1;
            else
                start = mid + 1;
        }
        result.push_back(lower_bound);
        result.push_back(upper_bound);
        return result;
    }
};