class Solution:
    def dfs(self, i, j, rows, cols, grid):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
            return
        grid[i][j] = '2'
        self.dfs(i, j+1, rows, cols, grid)
        self.dfs(i, j-1, rows, cols, grid)
        self.dfs(i+1, j, rows, cols, grid)
        self.dfs(i-1, j, rows, cols, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, rows, cols, grid)
        return count