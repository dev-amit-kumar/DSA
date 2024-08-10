# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        inorder = sorted(self.abc(root))
        for i in range(1,len(inorder)):
            if inorder[0] < inorder[i]:
                return inorder[i]
        return -1
    def abc(self, root):
        if root is None:
            return []
        return self.abc(root.left) + [root.val] + self.abc(root.right)
        
        