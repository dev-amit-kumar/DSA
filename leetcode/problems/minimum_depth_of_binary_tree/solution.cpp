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
    int dfs(TreeNode* root){
        if(root == NULL)
            return 0;
        else if(root -> left == NULL)
            return 1 + dfs(root -> right);
        else if(root -> right == NULL)
            return 1 + dfs(root -> left);
        else
            return 1 + min(dfs(root -> left),  dfs(root -> right));
    }
    int minDepth(TreeNode* root) {
        return dfs(root);
    }
};