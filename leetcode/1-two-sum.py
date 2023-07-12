# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keep = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in keep:
                return [keep[k], i]
            else:
                keep[nums[i]] = i
