# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        n = len(preorder)
        for i in range(1, n):
            value = preorder[i]
            newNode = TreeNode(value)
            if preorder[i] < stack[-1].val:
                stack[-1].left = newNode
            else:
                while stack and stack[-1].val < preorder[i]:
                    last = stack.pop()
                last.right = newNode
            stack.append(newNode)
        return root