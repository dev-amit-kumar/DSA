class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row_arr = [1] * row
        col_arr = [1] * col
        for i in range(0, row):
            for j in range(0, col):
                if(matrix[i][j] == 0):
                    row_arr[i] = 0
                    col_arr[j] = 0
        for i in range(0, row):
            for j in range(0, col):
                if(row_arr[i]==0 or col_arr[j]==0):
                    matrix[i][j] = 0
        