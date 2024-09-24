class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()

        def dfs(u, v):
            if u == v:
                return True
            for w in graph[u]:
                if w not in visited:
                    visited.add(w)
                    if dfs(w, v):
                        return True
                    visited.remove(w)
            return False

        for u, v in edges:
            if dfs(u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)

        return []