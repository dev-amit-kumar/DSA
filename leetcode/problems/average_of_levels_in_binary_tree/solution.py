class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root]
        while(q):
            temp = 0
            qlen = len(q)
            for i in range(qlen):
                curr = q.pop(0)
                temp += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(temp/qlen)
        return res