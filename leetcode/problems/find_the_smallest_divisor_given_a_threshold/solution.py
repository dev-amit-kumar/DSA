import math
class Solution:
    # def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    #     total = []
    #     for i in range(1, max(nums)+1):
    #         curr = 0
    #         for j in nums:
    #             curr += math.ceil(j / i)
    #         if(curr <= threshold):
    #             total.append(i)
    #     return min(total)
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while(l <= r):
            mid = (l + r) // 2
            curr = 0
            for j in nums:
                curr += math.ceil(j / mid)
            if (curr <= threshold):
                r = mid - 1
            else:
                l = mid + 1
        return l