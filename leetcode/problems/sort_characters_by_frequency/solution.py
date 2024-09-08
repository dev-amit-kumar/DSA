class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        heap = []
        for char, freq in freq.items():
            heapq.heappush(heap, (-freq, char))
        result = ''
        while(heap):
            freq, char = heapq.heappop(heap)
            result += (-freq * char)
        return result