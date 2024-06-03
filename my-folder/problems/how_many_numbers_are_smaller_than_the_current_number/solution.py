class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            curr = 0
            for j in range(0, len(nums)):
                if (nums[i] > nums[j] and i != j):
                    curr += 1
            result.append(curr)
        return result