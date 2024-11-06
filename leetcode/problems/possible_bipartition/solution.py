class Solution:
    def bfs(self, node, adj, color):
        q = deque()
        q.append(node)
        color[node] = 0
        while q:
            top = q.popleft()
            for it in adj[top]:
                if color[it] == -1:
                    color[it] = 1 - color[top]
                    q.append(it)
                elif color[it] == color[top]:
                    return False
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for a, b in dislikes:
            adj_list[a - 1].append(b - 1)
            adj_list[b - 1].append(a - 1)
        color = [-1] * n
        for i in range(n):
            if color[i] == -1:
                if not self.bfs(i, adj_list, color):
                    return False
        return True