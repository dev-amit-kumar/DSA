// https://leetcode.com/problems/permutations/

#include <iostream>
#include <vector>
using namespace std;

void DFS(vector<int> &nums, int pos, vector<int> &vec, vector<vector<int>> &res)
{
    if (pos == nums.size())
    {
        res.push_back(vec);
        return;
    }
    for (int i = 0; i <= vec.size(); i++)
    {
        vec.insert(vec.begin() + i, nums[pos]);
        DFS(nums, pos + 1, vec, res);
        vec.erase(vec.begin() + i);
    }
    return;
}

vector<vector<int>> permute(vector<int> &nums)
{
    vector<vector<int>> res;
    vector<int> vec;
    DFS(nums, 0, vec, res);
    return res;
}

int main()
{
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> ans = permute(nums);
    for (int i = 0; i <= ans.size(); i++)
    {
        for (int j = 0; j <= ans[i].size(); j++)
            cout << ans[i][j] << ' ';
    }
}