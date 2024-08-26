# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_val = 0
    def dfs(self, root):
        if not root: return (True, 0, None, None)
        is_left_bst, left_sum, left_min, left_max = self.dfs(root.left)
        is_right_bst, right_sum, right_min, right_max = self.dfs(root.right)
        if is_left_bst and is_right_bst and (not left_max or left_max < root.val) and (not right_min or right_min > root.val):
            curr_sum = left_sum + right_sum + root.val
            self.max_val = max(self.max_val, curr_sum)
            return (True, curr_sum, left_min or root.val, right_max or root.val)
        else:
            return (False, 0, None, None)

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_val