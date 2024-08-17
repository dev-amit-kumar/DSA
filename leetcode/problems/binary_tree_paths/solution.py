# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, currPath):
            if len(currPath) > 0:
                currPath += "->" + str(root.val)
            else:
                currPath = str(root.val)
            if root.left is None and root.right is None:
                ans.append(currPath)
                return
            if root.left:
                helper(root.left, currPath)
            if root.right:
                helper(root.right, currPath)
        ans = []
        helper(root, '')
        return ans