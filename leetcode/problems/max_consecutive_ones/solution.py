class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        currCount = 0
        for i in nums:
            if i == 1:
                currCount += 1
            elif i == 0:
                count = max(count, currCount)
                currCount = 0
        count = max(count, currCount)
        return count