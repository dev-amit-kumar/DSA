class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [([0]* len(colSum)) for i in range(len(rowSum))]
        i = 0
        j = 0
        r = len(rowSum)
        c = len(colSum)
        while(i < r and j < c):
            val = min(rowSum[i], colSum[j])
            matrix[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val
            if(rowSum[i] == 0):
                i += 1
            else:
                j += 1
        return matrix
