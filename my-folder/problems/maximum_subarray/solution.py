class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        overAllSum = float('-inf')
        for i in nums:
            if(currSum + i > i):
                currSum += i
            else:
                currSum = i
            overAllSum = max(overAllSum, currSum)
        return overAllSum