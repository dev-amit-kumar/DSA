class Solution(object):
    def numIslands(self, grid):
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return 0
            
            grid[r][c] = '0'
            
            for i, j in zip((r - 1, r + 1, r, r), (c, c, c - 1, c + 1)):
                dfs(i, j)
            
            return 1
        
        return sum(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
        