class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCnt = [0] * n
        for i in trust:
            trustCnt[i[0] - 1] -= 1
            trustCnt[i[1] - 1] += 1
        for i in range(n):
            if trustCnt[i] == n - 1:
                return i + 1
        return -1