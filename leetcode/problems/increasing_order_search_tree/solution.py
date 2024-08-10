# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getList (self, root):
        if not root:
            return []
        return self.getList(root.left) + [root.val] + self.getList(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = self.getList(root)
        root = TreeNode(result[0])
        temp = root
        for i in result[1:]:
            newNode = TreeNode(i)
            temp.right = newNode
            temp = temp.right
        return root