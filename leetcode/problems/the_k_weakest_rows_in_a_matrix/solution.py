class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(0, len(mat)):
            heapq.heappush(heap, (sum(mat[i]), i))
        result = []
        for _ in range(k):
            val = heapq.heappop(heap)
            result.append(val[1])
        return result