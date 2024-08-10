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
    int helper(TreeNode * root, int height){
        if(root == NULL)
            return height;
        height += 1;
        int left = helper(root->left, height);
        int right = helper(root->right, height);
        return max(left, right);
    }

    int maxDepth(TreeNode* root) {
        return helper(root, 0);
    }
};