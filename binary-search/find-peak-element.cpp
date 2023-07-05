// https://leetcode.com/problems/find-peak-element

#include <iostream>
#include <vector>
using namespace std;

int search(vector<int> &nums, int target)
{
    int start = 0;
    int end = nums.size() - 1;
    int mid;
    while (start <= end)
    {
        mid = (start + end) / 2;
        if (nums[mid] > nums[mid + 1])
            end = mid;
        else
            start = mid + 1;
    }
    return start;
}

int main()
{
    vector<int> nums = {978, 979, 980, 981, 982, 986, 987, 988, 990, 992, 994, 995, 997};
    int result = search(nums, 988);
    cout << result << endl;
}