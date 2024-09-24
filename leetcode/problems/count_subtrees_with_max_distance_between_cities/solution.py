class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        lookup = [[] for _ in range(n+1)]
        for u, v in edges:
            lookup[u].append(v)
            lookup[v].append(u)

        def get_max_distance(tree):
            root = 0
            for i in range(1, n+1):
                if (1 << i) & tree:
                    root = i
                    break
            distance = 0
            fathers = set([root])
            def dp(node): # get max path length ending with this node
                nonlocal distance
                childs = []
                for next in lookup[node]:
                    if (1 << next) & tree:
                        if next in fathers:
                            continue
                        fathers.add(next)
                        childs.append(dp(next))
                if len(childs) == 0:
                    return 0
                if len(childs) == 1:
                    distance = max(distance, childs[0] + 1)
                    return childs[0] + 1
                
                childs.sort()
                # get max path pass through this node
                distance = max(distance, childs[-1] + childs[-2] + 2)
                return childs[-1] + 1

            dp(root)
            return distance
        
        q = deque()
        visited = set()
        for i in range(1, n+1):
            q.append(1 << i)
            visited.add(1 << i)
        res = [0 for _ in range(n - 1)]
        while q:
            cur = q.popleft()
            if cur.bit_count() > 1:
                res[get_max_distance(cur)-1] += 1

            for u, v in edges:
                uin, vin = (1 << u) & cur, (1 << v) & cur
                if uin and vin:
                    continue
                if (not uin) and (not vin):
                    continue
                if uin:
                    next = cur | (1 << v)
                    if next not in visited:
                        visited.add(next)
                        q.append(next)
                elif vin:
                    next = cur | (1 << u)
                    if next not in visited:
                        visited.add(next)
                        q.append(next)

        return res