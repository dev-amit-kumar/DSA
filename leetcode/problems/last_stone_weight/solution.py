class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x * -1 for x in stones]
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1: return stones[0] * -1
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            if x == y: continue
            elif x != y: heapq.heappush(stones, abs(y - x) * -1)
        return 0