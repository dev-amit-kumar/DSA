class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node):
            visited[node] = True
            for adj in adjList[node]:
                if not visited[adj]:
                    dfs(adj)
                elif adj in result:
                    result.remove(adj)

        adjList = [[] for _ in range(n)]
        for edge in edges:
            u,v = edge
            adjList[u].append(v)
        
        result = set()
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                dfs(i)
                result.add(i)
        return list(result)