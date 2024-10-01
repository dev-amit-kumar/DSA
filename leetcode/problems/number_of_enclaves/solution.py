class Solution:
    def dfs(self, i, j, rows, cols, grid):
        if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.dfs(i+1, j, rows, cols, grid)
        self.dfs(i-1, j, rows, cols, grid)
        self.dfs(i, j+1, rows, cols, grid)
        self.dfs(i, j-1, rows, cols, grid)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i * j == 0 or i == rows - 1 or j == cols - 1:
                    if grid[i][j] == 1:
                        self.dfs(i, j, rows, cols, grid)
        ans = 0
        for row in grid:
            ans += sum(row)
        return ans