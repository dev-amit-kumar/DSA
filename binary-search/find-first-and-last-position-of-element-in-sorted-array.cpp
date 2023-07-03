// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

#include <iostream>
#include <vector>
using namespace std;

vector<int> searchRange(vector<int> &nums, int target)
{
    int start = 0;
    int end = nums.size() - 1;
    int mid;
    int lower_bound = 0;
    int upper_bound = 0;
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
}

int main()
{
    vector<int> nums = {5, 7, 7, 8, 8, 8, 8, 8, 10};
    vector<int> result = searchRange(nums, 8);
    for (int i = 0; i <= result.size(); i++)
        cout << result[i] << endl;
}