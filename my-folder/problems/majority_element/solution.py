class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() # sorting the elements of array 
        return nums[len(nums) // 2]