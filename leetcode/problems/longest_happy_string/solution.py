class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        last = None
        heap = []
        if a > 0: heapq.heappush(heap, (-a,'a'))
        if b > 0: heapq.heappush(heap, (-b,'b'))
        if c > 0: heapq.heappush(heap, (-c,'c'))
        while heap:
            (count, char) = heapq.heappop(heap)
            if count == -1 or last and last[0] < count:
                count += 1
                ans += [char]
            else:
                count += 2
                ans += [char] * 2
            if last:
                heapq.heappush(heap, last)
            if count == 0:
                last = None
            else:
                last = (count, char)
        return ''.join(ans)