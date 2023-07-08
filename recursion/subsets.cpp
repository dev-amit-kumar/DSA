// https://leetcode.com/problems/subsets/

#include <iostream>
#include <vector>

vector<vector<int>> ans;
void recursiveCall(vector<int> &nums, vector<int> currSubSet, int i)
{
    if (i == nums.size())
    {
        ans.push_back(currSubSet);
        return;
    }
    recursiveCall(nums, currSubSet, i + 1);
    currSubSet.push_back(nums[i]);
    recursiveCall(nums, currSubSet, i + 1);
}

vector<vector<int>> subsets(vector<int> &nums)
{
    vector<int> temp;
    recursiveCall(nums, temp, 0);
    return ans;
}

int main()
{
    vector<int> nums = {1, 2, 3};
    for (auto subset : ans)
    {
        for (auto i : subset)
            cout << i << ' ';
    }
}