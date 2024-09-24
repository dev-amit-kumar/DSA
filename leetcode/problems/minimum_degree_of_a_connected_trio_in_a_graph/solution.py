class Solution:
    def minTrioDegree(self, n, edges):
        graph, indegree, min_val = defaultdict(set), defaultdict(int), float("inf")

        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
            indegree[i] += 1 
            indegree[j] += 1 

        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if j in graph[i]:
                    for k in range(j+1,n+1):
                        if k in graph[j] and i in graph[k]:
                            min_val = min(min_val,indegree[i]+indegree[j]+indegree[k]-6)

        return min_val if min_val != float("inf") else -1