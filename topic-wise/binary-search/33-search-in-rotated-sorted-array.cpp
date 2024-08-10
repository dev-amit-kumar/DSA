// https://leetcode.com/problems/search-in-rotated-sorted-array/

#include <iostream>
#include <vector>
using namespace std;

int search(vector<int> &nums, int target)
{
    int n = nums.size();
    int start = 0;
    int end = n - 1;
    while (start <= end)
    {
        int mid = (start + end) / 2;
        if (nums[mid] == target)
            return mid;
        if (nums[start] <= nums[mid]) // left half is sorted
        {
            if (target >= nums[start] && target <= nums[mid]) // element exists:
                end = mid - 1;
            else // element does not exist:
                start = mid + 1;
        }
        else // right half is sorted
        {
            if (nums[mid] <= target && target <= nums[end]) // element exists:
                start = mid + 1;
            else // element does not exist:
                end = mid - 1;
        }
    }
    return -1;
}

int main()
{
    vector<int> arr = {4, 5, 6, 7, 0, 1, 2};
    int result = search(arr, 4);
    cout << "result " << result << endl;
}