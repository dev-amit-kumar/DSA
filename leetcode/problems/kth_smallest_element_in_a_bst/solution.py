# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = self.abc(root)
        return inorder[k-1]
    def abc(self, root):
        if root is None:
            return []
        return self.abc(root.left) + [root.val] + self.abc(root.right)
        