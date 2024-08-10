class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l ==1:
            return nums[0]        
        start = 0
        end = l -1
   
        while start < end:
            mid = (start + end)//2
            if nums[mid] > nums[end]:
                start = mid +1
            else:
                end = mid
        return nums[start]