/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameter(TreeNode *root, int &ans)
    {
        if (root == NULL)
            return 0;

        int lh = diameter(root->left, ans);
        int rh = diameter(root->right, ans);
        ans = max(ans, lh + rh);
        return 1 + max(lh, rh);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int max = 0;
        diameter(root, max);
        return max;
    }
};