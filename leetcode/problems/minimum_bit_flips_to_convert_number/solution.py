class Solution(object):
    def minBitFlips(self, start, goal):
        res = start ^ goal
        cnt = 0
        while res:
            res &= res - 1
            cnt += 1
        return cnt