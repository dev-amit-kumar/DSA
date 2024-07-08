class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        visit = {}
        ans = []
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if i/j not in visit:
                    visit[i/j] = 1
                    ans.append("{}/{}".format(i,j))
        return ans