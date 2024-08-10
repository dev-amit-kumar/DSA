class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(0, len(nums)):
            value = nums[nums[i]]
            new_nums.append(value)
        return new_nums