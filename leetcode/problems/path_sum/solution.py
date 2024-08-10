# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        else:
            sum = sum - root.val
            if root.left is None and root.right is None and (sum == 0):
                return True
            else:
                return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)