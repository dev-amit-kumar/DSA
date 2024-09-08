from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        if k == len(nums): return nums
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))
        result = []
        while (k > 0 and heap):
            freq, num = heapq.heappop(heap)
            result.append(num)
            k -= 1
        return result