class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        new_array = sorted(nums)
        idx = len(nums)-1
        for i in range(1, len(new_array), 2):
            nums[i] = new_array[idx]
            idx -= 1
        for i in range(0, len(new_array), 2):
            nums[i] = new_array[idx]
            idx -= 1
