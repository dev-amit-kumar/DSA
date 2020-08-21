class Solution:
    def climbStairs(self, n: int) -> int:
        pre_1, pre_2 = 2, 1
        if n <= 1:
            return pre_2
        cur = pre_1
        for i in range(3, n+1):
            cur = pre_1 + pre_2
            pre_1, pre_2 = cur, pre_1
        return cur