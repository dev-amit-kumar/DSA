import heapq
from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pq = []
        sum = 0
        min_len = float('inf')

        for i, num in enumerate(nums):
            sum += num
            if sum >= k:
                min_len = min(min_len, i + 1)
            while pq and sum - pq[0][0] >= k:
                min_len = min(min_len, i - heapq.heappop(pq)[1])
            heapq.heappush(pq, (sum, i))

        return min_len if min_len != float('inf') else -1