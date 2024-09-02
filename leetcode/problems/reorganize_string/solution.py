class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = []
        for char, count in counts.items():
            heapq.heappush(max_heap, (-count, char))
        prev_char = None
        prev_count = 0
        result = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            count += 1
            prev_char = char
            prev_count = count
        return "" if len(result) != len(s) else "".join(result)