# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None :
            return [] 
        result = defaultdict(list)
        queue = list()
        level = 0
        queue.append((root, level))
        while len(queue) > 0:
            x,l = queue.pop(0)
            result[l].append(x.val)
            level = l+1
            if x.left is not None:
                queue.append((x.left, level))
            if x.right is not None:
                queue.append((x.right, level))
        ans = list(result.values())
        return ans