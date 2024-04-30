class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(r, c, heights, arr, prev):
            if(r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in arr or heights[r][c] < prev): return
            arr.add((r, c))
            dfs(r+1, c, heights, arr, heights[r][c])
            dfs(r-1, c, heights, arr, heights[r][c])
            dfs(r, c+1, heights, arr, heights[r][c])
            dfs(r, c-1, heights, arr, heights[r][c])


        rows = len(heights)
        cols = len(heights[0])
        atl = set()
        pac = set()
        result = []
        for c in range(0, cols):
            dfs(0, c, heights, pac, heights[0][c])
            dfs(rows-1, c, heights, atl, heights[rows-1][c])
        
        for r in range(0, rows):
            dfs(r, 0, heights, pac, heights[r][0])
            dfs(r, cols-1, heights, atl, heights[r][cols-1])

        for r in range(0, rows):
            for c in range(0, cols):
                if(r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result