class Solution {
public:
    void backtrack(vector<int> &curr, vector<vector<int>> &ans, int k, int pos, int target)
    {
        if (curr.size() == k && target == 0)
        {
            ans.push_back(curr);
            return;
        }
        for (int i = pos; i <= 9; i++)
        {
            if (!binary_search(curr.begin(), curr.end(), i))
            {
                curr.push_back(i);
                backtrack(curr, ans, k, i + 1, target - i);
                curr.pop_back();
            }
        }
    }

    vector<vector<int>> combinationSum3(int k, int n)
    {
        vector<vector<int>> ans;
        vector<int> curr;
        backtrack(curr, ans, k, 1, n);
        return ans;
    }
};