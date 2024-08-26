# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isIdentitical(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if root1.val != root2.val: return False
        left = self.isIdentitical(root1.left, root2.left)
        right = self.isIdentitical(root1.right, root2.right)
        return True and left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        ans = False
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == subRoot.val:
                ans = ans or self.isIdentitical(node, subRoot)
            if node.left: 
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)
        return ans