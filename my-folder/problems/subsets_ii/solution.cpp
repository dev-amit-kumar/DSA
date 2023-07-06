class Solution {
public:
    void recursiveCall(vector<int> &nums, vector<int> temp, int pos, vector<vector<int>> &ans)
    {
        ans.push_back(temp);
        for (int i = pos; i < nums.size(); i++)
        {
            if (i > pos && nums[i] == nums[i - 1])
                continue;
            temp.push_back(nums[i]);
            recursiveCall(nums, temp, i + 1, ans);
            temp.pop_back();
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        vector<int> temp;
        vector<vector<int>> ans;
        recursiveCall(nums, temp, 0, ans);
        return ans;
    }
};