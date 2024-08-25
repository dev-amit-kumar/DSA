# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, prev):
        if not root:
            return True
        if root.val == prev:
            left = self.helper(root.left, root.val)
            right = self.helper(root.right, root.val)
            return True and left and right
        else:
            return False

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root, root.val)