class Solution:
    def dfs(self, visited, adjList, node):
        visited[node] = True
        for i in adjList[node]:
            if not visited[i]:
                self.dfs(visited, adjList, i)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n -1:
            return -1
        adjList = [[] for _ in range(n)]
        for u, v in connections:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(visited, adjList, i)
        return count-1