class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False

        visited = set()
        return dfs(source, visited)