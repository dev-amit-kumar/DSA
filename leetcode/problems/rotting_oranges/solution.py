class Solution:
    def dfs(self, grid, i, j, minutes):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (grid[i][j] > 1 and grid[i][j] < minutes):
            return
        grid[i][j] = minutes
        self.dfs(grid, i, j+1, minutes+1)
        self.dfs(grid, i, j-1, minutes+1)
        self.dfs(grid, i-1, j, minutes+1)
        self.dfs(grid, i+1, j, minutes+1)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    self.dfs(grid, i, j, 2)
        count = 2
        for i in grid:
            for j in i:
                if j == 1: return -1
                else: count = max(count, j)
        return count - 2