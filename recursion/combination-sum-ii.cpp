// https://leetcode.com/problems/combination-sum-ii/

#include <iostream>
#include <vector>
using namespace std;

void backtrack(vector<vector<int>> &ans, vector<int> &curr, vector<int> &candidates, int target, int pos)
{
    if (target == 0)
    {
        ans.push_back(curr);
        return;
    }
    for (int i = pos; i < candidates.size(); i++)
    {
        if (i > pos && candidates[i] == candidates[i - 1])
            continue;
        if (target - candidates[i] < 0)
            break;
        curr.push_back(candidates[i]);
        backtrack(ans, curr, candidates, target - candidates[i], i + 1);
        curr.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
{
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> ans;
    vector<int> curr;
    backtrack(ans, curr, candidates, target, 0);
    return ans;
}

int main()
{
    vector<int> candidates = {10, 1, 2, 7, 6, 1, 5};
    int target = 8;
    vector<vector<int>> arr = combinationSum2(candidates, target);
    cout << "result" << endl;
    for (vector<int> arr1 : arr)
    {
        for (int i : arr1)
            cout << i << " ";
        cout << endl;
    }
}