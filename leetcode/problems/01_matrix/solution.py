class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >= m:
            return False
        return True

    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        n = len(grid)
        m = len(grid[0])

        visited = [[0 for _ in range(m)] for _ in range(n)]
        distance = [[0 for _ in range(m)] for _ in range(n)]
        
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        while(q):
            row, col, dist = q.popleft()
            if visited[row][col] == 0:
                distance[row][col] = dist
                visited[row][col] = 1
                for i in range(4):
                    nRow = row + delRow[i]
                    nCol = col + delCol[i]
                    if self.isValid(nRow, nCol, n, m):
                        q.append((nRow, nCol, dist+1))
        
        return distance