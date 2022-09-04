class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        count = 0
        while g and s:
            if s[-1] >= g[-1]:
                count += 1
                s.pop()
                g.pop()
            else:
                s.pop()
        return count