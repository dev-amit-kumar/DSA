class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if words is None: return []
        freq_map = Counter(words)
        minHeap = []
        for word, freq in freq_map.items():
            heapq.heappush(minHeap, (-freq, word))
        result = []
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])
        return result