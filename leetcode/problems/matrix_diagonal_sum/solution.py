class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        mid = n//2
        for i in range(0, n):
            total += mat[i][i] + mat[i][n-i-1]
        if(n%2 == 1):
            total -= mat[mid][mid]
        return total