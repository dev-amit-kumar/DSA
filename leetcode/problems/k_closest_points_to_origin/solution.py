class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x*x + y*y
            heap.append((distance, x, y))
        heapq.heapify(heap)
        ans = []
        while k > 0:
            distance, x, y = heapq.heappop(heap)
            ans.append((x,y))
            k -= 1
        return ans