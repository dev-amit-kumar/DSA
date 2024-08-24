class Solution:
    total_tilt = 0
    def helper(self, node):
        if not node: return 0
        ls, rs = self.helper(node.left), self.helper(node.right)
        self.total_tilt += abs(ls - rs)
        return ls + rs + node.val
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.total_tilt