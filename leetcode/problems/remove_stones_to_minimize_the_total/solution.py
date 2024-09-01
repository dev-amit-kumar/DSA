class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles = [x * -1 for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            top = heapq.heappop(piles)
            dec = math.floor(-top/2)
            total -= dec
            heapq.heappush(piles, top + dec)
        return sum(piles) * -1
