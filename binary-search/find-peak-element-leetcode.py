# https://leetcode.com/problems/find-peak-element/

# Using Linear Search Approach, O(n)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(0, l-1):
            if (nums[i] > nums[i+1]):
                return i
        return l-1

# Using Binary Search Approach, O(logn)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while (start < end):
            mid = (start + end)//2
            if (nums[mid] > nums[mid+1]):
                end = mid
            else:
                start = mid + 1
        return start
