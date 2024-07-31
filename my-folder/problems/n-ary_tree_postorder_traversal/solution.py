"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def recursive(root, stack):
            if not root:
                return
            for i in root.children:
                recursive(i, stack)
            stack.append(root.val)
        stack = []
        recursive(root, stack)
        return stack