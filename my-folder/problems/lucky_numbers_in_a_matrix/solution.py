class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for r in range(0, rows):
            ans = matrix[r][0]
            index = 0
            for c in range(0, cols):
                if(ans > matrix[r][c]):
                    ans = matrix[r][c]
                    index = c
            isMax = True
            for rr in range(0, rows):
                if(ans < matrix[rr][index]):
                    isMax = False
                    break
            if (isMax):
                result.append(ans)
        return result