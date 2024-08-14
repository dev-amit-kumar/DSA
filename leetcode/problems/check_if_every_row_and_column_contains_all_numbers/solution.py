class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        lenMatrix = len(matrix)
        for i in range(lenMatrix):
            lineSet = set()
            for j in range(lenMatrix):
                if matrix[i][j] in lineSet:
                    return False
                lineSet.add(matrix[i][j])

        for j in range(lenMatrix):
            columnSet = set()
            for i in range(lenMatrix):
                if matrix[i][j] in columnSet:
                    return False
                columnSet.add(matrix[i][j])
        return True