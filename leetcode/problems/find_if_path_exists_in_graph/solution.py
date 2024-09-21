class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False] * n
        visited[source] = True
        queue = deque([source])

        while queue:
            temp = queue.popleft()
            if temp == destination:
                return True
            for connect in adj_list[temp]:
                if not visited[connect]:
                    visited[connect] = True
                    queue.append(connect)

        return False