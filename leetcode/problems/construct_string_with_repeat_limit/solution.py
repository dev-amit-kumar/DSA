class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(key), value) for key, value in Counter(s).items()]
        heapq.heapify(heap)
        ans = ""
        while heap:
            key, value = heapq.heappop(heap)
            if value <= repeatLimit:
                ans += chr(-key) * value
            else:
                ans += chr(-key) * repeatLimit
                if not heap:
                    break
                new_key, new_value = heapq.heappop(heap)
                ans += chr(-new_key)
                if new_value > 1:
                    heapq.heappush(heap, (new_key, new_value - 1))
                heapq.heappush(heap, (key, value - repeatLimit))
        return ans