class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapify(heap)
        count = 0
        while len(heap) > 1:
            first, sec = heappop(heap) + 1, heappop(heap) + 1
            count += 1
            if first < 0: heappush(heap, first)
            if sec < 0: heappush(heap, sec)
        return count