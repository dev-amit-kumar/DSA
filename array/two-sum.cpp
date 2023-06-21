// https://leetcode.com/problems/two-sum/

// Input : nums = [ 2, 7, 11, 15 ], target = 9 Output : [ 0, 1 ]
// Explanation : Because nums[0] + nums[1] == 9, we return [ 0, 1 ].

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int> &nums, int target)
{
    unordered_map<int, int> mp;
    for (int i = 0; i < nums.size(); i++)
    {
        int temp = target - nums[i];
        if (mp.find(temp) == mp.end()) // element not found
            mp[nums[i]] = i;
        else // element found
            return {mp[temp], i};
    }
    return {-1, -1};
}

int main()
{
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    for (int i = 0; i < result.size(); i++)
        cout << result[i] << " ";
    cout << endl;
    return 0;
}
