// https://leetcode.com/problems/sort-colors/

// This problem is a variation of the popular Dutch National flag algorithm.

class Solution
{
public:
    void sortColors(vector<int> &nums)
    {
        int len = nums.size();
        int low = 0, mid = 0, high = len - 1;
        while (mid <= high)
        {
            if (nums[mid] == 0)
            {
                swap(nums[low], nums[mid]);
                mid++;
                low++;
            }
            else if (nums[mid] == 1)
            {
                mid++;
            }
            else
            {
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};