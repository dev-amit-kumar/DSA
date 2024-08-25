# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total = float('-inf')
    def helper(self, root):
        if not root: return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.total = max(self.total, root.val + left + right)
        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.total