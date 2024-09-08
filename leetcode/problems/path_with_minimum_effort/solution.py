class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        cost_freq = dict()
        for i in range(m):
            for j in range(n):
                cost_freq[(i, j)] = float('inf')
        
        heap = [[0, 0, 0]]
        while heap:
            cost, i, j = heappop(heap)
            if i == m - 1 and j == n - 1:
                return cost
            if cost >= cost_freq[(i, j)]:
                continue
            cost_freq[(i, j)] = cost

            for r, c in moves:
                row = i + r
                col = j + c
                if 0 <= row < m and 0 <= col < n:
                    curr_cost = abs(heights[i][j] - heights[row][col])
                    heappush(heap, [max(cost, curr_cost), row, col])