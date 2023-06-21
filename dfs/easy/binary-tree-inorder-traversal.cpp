// Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

// Solutions: https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/1377500/3-solutions-1-recursive-2-iterative-o-1-space-complexity-morris-traversal-explained-code/

// recursive approach
vector<int> helper(TreeNode *root, int &ans)
{
    if (root == NULL)
        return;
    helper(root->left, ans);
    ans.push_back(root->val);
    helper(root->right, ans);
}

vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> ans;
    helper(root, ans);
    return ans;
}

// use a stack
vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> ans;
    stack<TreeNode *> s;
    while (root || !s.empty())
    {
        if (root != NULL)
        {
            s.push(root);
            root = root->left;
        }
        else
        {
            root = s.top();
            s.pop();
            ans.push_back(root->val);
            root = root->right;
        }
    }
    return ans;
}

// morris algo

vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> ans;
    TreeNode *temp;
    while (root)
    {
        if (root->left)
        {
            temp = root->left;
            while (temp->right)
            {
                temp = temp->right;
            }
            temp->right = root;
            temp = root->left;
            root->left = NULL;
            root = temp;
        }
        else
        {
            ans.push_back(root->val);
            root = root->right;
        }
    }
    return ans;
}