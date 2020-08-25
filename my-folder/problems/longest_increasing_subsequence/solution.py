class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1]*n
        for i in range (1, n):
            for j in range (0, i):
                if nums[i] > nums[j] and arr[i]< arr[j] + 1 :
                    arr[i] = arr[j]+ 1
        maximum = 0
        for i in range (n):
            maximum = max (maximum , arr[i])
        return maximum