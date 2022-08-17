class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = []
        for i in range(0, len(nums)):
            total = 0
            for j in range(0, i+1):
                total += nums[j]
            sum.append(total)
        return sum