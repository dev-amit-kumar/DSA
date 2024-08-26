# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Unmonitored (0)
# Monitored and has Camera (1)
# Monitored and doesn't have a Camera (2)
# Leaf nodes (infinity)

class Solution:
    def postOrder(self, node):
        if not node: return (0, math.inf)
        l_count, l_state = self.postOrder(node.left)
        r_count, r_state = self.postOrder(node.right)
        state = min(l_state, r_state)
        total_cameras = l_count + r_count

        if state == 0:
            return (total_cameras + 1, 1)
        elif state == 1:
            return (total_cameras, 2)
        return (total_cameras, 0)

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        dummy = TreeNode(-1, root)
        return self.postOrder(dummy)[0]