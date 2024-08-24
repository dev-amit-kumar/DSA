# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            p_top, q_top = stack.pop()
            if not p_top and not q_top:
                continue
            if not p_top or not q_top:
                return False
            if p_top.val != q_top.val:
                return False
            stack.append((p_top.left, q_top.left))
            stack.append((p_top.right, q_top.right))
        return True