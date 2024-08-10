class Solution:
    def generate(self, r: int) -> List[List[int]]:
        if(r == 0): return []
        result = []
        result.append([1])
        for i in range(1, r):
            res = [1]
            for j in range(1, i):
                res.append(result[i-1][j-1] + result[i-1][j])
            res.append(1)
            result.append(res)
        return result