// https://leetcode.com/problems/combination-sum/

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
    if (target < 0)
        return;
    for (int i = pos; i < candidates.size(); i++)
    {
        curr.push_back(candidates[i]);
        backtrack(ans, curr, candidates, target - candidates[i], i);
        curr.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int> &candidates, int target)
{
    vector<vector<int>> ans;
    vector<int> curr;
    backtrack(ans, curr, candidates, target, 0);
    return ans;
}

int main()
{
    vector<int> candidates = [ 1, 2, 3, 4, 5 ];
    int target = 8;
    vector<vector<int>> arr = combinationSum(candidates, target);
    cout << "result" << endl;
    for (vector<int> arr1 : arr)
    {
        for (int i : arr1)
            cout << i << " ";
        cout << endl;
    }
}