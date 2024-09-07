class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        heap = []
        hash_map = Counter(arr)
        for key, values in hash_map.items():
            heapq.heappush(heap, (-values, key))
        curr = 0
        res = 0
        while curr < n / 2 and heap:
            values, key = heapq.heappop(heap)
            curr += (-values)
            res += 1
        return res