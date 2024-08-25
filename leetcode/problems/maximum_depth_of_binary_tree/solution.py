# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS using deque
        if not root: return 0
        treeQueue = deque([root])
        depth = 0
        while treeQueue:
            nodeCount = len(treeQueue)
            for _ in range(nodeCount):
                temp = treeQueue.popleft()
                if temp.left:
                    treeQueue.append(temp.left)
                if temp.right:
                    treeQueue.append(temp.right)
            depth += 1
        return depth