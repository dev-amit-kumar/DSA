# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        stack = [(root1, root2)]
        while(stack):
            root1_dup, root2_dup = stack.pop()
            val = 0
            if not root1_dup or not root2_dup: continue
            root1_dup.val += root2_dup.val
            if not root1_dup.left:
                root1_dup.left = root2_dup.left
            else:
                stack.append((root1_dup.left, root2_dup.left))
            if not root1_dup.right:
                root1_dup.right = root2_dup.right
            else:
                stack.append((root1_dup.right, root2_dup.right))
        return root1