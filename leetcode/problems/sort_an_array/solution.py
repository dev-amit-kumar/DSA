class Solution:
    def sortArray(self, nums):
        heapq.heapify(nums)
        result = []
        while nums:
            result.append(heapq.heappop(nums))
        return result