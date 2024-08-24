# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left - right) > 1 or left == -1 or right == -1: return -1
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1