// Link: https://leetcode.com/problems/path-sum/

bool dfs(TreeNode *root, int targetSum, int &currSum)
{
    if (root == NULL)
        return false;
    int val = root->val;
    currSum += val;
    if (root->left == NULL && root->right == NULL)
    {
        if (currSum == targetSum)
            return true;
        currSum -= val;
        return false;
    }
    bool left = dfs(root->left, targetSum, currSum);
    bool right = dfs(root->right, targetSum, currSum);
    if (left || right)
        return true;
    currSum -= val;
    if (!left)
        return false;
    if (!right)
        return false;
    return true;
}
bool hasPathSum(TreeNode *root, int targetSum)
{
    int sum = 0;
    return dfs(root, targetSum, sum);
}

// Optimize solution
bool dfs(TreeNode *root, int targetSum)
{
    if (root == NULL)
        return false;
    targetSum -= root->val;
    if (root->left == NULL && root->right == NULL && targetSum == 0)
        return true;
    return dfs(root->left, targetSum) || dfs(root->right, targetSum);
}
bool hasPathSum(TreeNode *root, int targetSum)
{
    return dfs(root, targetSum);
}