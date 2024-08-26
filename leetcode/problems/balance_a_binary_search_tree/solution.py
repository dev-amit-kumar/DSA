# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if not root: return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def buildBST(self, values):
        if not values: return None
        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = self.buildBST(values[:mid])
        root.right = self.buildBST(values[mid+1:])
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        inOrderValues = self.inOrder(root)
        return self.buildBST(inOrderValues)
