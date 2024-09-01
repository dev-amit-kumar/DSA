class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if words is None: return []
        freq_map = {}
        minHeap = []
        result = []
        for i in words:
            if i in freq_map: freq_map[i] += 1
            else: freq_map[i] = 1
        for word, freq in freq_map.items():
            heapq.heappush(minHeap, (-freq, word))
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])
        return result