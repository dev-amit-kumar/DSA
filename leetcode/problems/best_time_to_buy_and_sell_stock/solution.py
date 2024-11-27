class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxTotal = 0
        minPrice = float("inf")
        n = len(prices)
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            maxTotal = max(maxTotal, prices[i] - minPrice)
        return maxTotal
