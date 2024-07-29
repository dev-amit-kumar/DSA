class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        idx = 0
        i = 1
        while(i <= n and idx < len(target)):
            ans.append("Push")
            if (i != target[idx]):
                ans.append("Pop")
            else:
                idx += 1
            i += 1
        return ans