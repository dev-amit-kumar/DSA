class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m = len(matrix)
        n = len(matrix[0])
        # calculate row-wise prefix xor
        for i in range(0, m):
            for j in range(1, n):
                matrix[i][j] ^= matrix[i][j-1]
        
        # calculate column-wise prefix xor
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] ^= matrix[i-1][j]
        
        for i in range(0, m):
            for j in range(0, n):
                heapq.heappush(heap, matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        return heap[0]