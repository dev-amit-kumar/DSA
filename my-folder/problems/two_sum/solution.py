class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            balance = target - nums[i]
            if balance in hashmap and hashmap[balance] != i:
                return [i, hashmap[balance]]
            hashmap[nums[i]] = i