class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda t: t[1])
        heap = []
        for (c, f, t) in trips:
            while heap and heap[0][0] <= f:
                v = heapq.heappop(heap)
                capacity += v[1]
            if c > capacity:
                return False
            capacity -= c
            heapq.heappush(heap, (t, c))
        return True