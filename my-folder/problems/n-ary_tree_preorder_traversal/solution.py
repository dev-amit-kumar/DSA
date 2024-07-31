"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def recursive(root, stack):
            if not root:
                return
            stack.append(root.val)
            for i in root.children:
                recursive(i, stack)
        stack = []
        recursive(root, stack)
        return stack