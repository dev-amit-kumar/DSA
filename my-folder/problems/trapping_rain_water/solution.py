class Solution:
    def trap(self, h: List[int]) -> int:
        suf = []
        pre = []
        temp = h[0]
        res = 0
        n = len(h) - 1
        for i in range(0, n):
            if (h[i] > temp):
                temp = h[i]
            pre.append(temp)

        temp = h[-1]
        for i in range(n, -1, -1):
            if (h[i] > temp):
                temp = h[i]
            suf.append(temp)

        for i in range(0, n):
            temp = min(pre[i], suf[n-i])
            res += temp - h[i]
        return res
