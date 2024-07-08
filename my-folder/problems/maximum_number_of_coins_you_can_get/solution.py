class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        ans = 0
        i = n//3
        while i < n:
            ans += piles[i]
            i += 2
        return ans