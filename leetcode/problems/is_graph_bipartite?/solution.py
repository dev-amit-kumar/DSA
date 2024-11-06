class Solution:
    def bfs(self, start, adj, color):
        q = deque()
        q.append(start)
        color[start] = 0
        while q:
            top = q.popleft()
            for it in adj[top]:
                if color[it] == -1:
                    color[it] = 1 - color[top]
                    q.append(it)
                elif color[it] == color[top]:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                if not self.bfs(i, graph, color):
                    return False
        return True