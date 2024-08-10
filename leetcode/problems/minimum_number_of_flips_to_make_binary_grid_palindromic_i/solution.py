class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        def min_flips_to_make_palindromic(line):
            flips = 0
            for i in range(len(line) // 2):
                if line[i] != line[-i-1]:
                    flips += 1
            return flips
        row_flips = sum(min_flips_to_make_palindromic(grid[i]) for i in range(m))
        col_flips = 0
        for j in range(n):
            column = [grid[i][j] for i in range(m)]
            col_flips += min_flips_to_make_palindromic(column)
        return min(row_flips, col_flips)