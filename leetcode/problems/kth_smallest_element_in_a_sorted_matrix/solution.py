class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for num in row:
                heapq.heappush(heap, -num)
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heap[0]