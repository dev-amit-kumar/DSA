class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u, v in roads:
            adjList[u].append(v)
            adjList[v].append(u)
        
        result = 0

        for i in range(n):
            for j in range(i+1, n):
                curr = len(adjList[i]) + len(adjList[j]) - int(i in adjList[j])
                result = max(result, curr)

        return result