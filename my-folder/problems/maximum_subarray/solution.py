class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        overall = float('-inf')
        for num in nums:
            if(currSum + num > num):
                currSum += num
            else:
                currSum = num
            overall = max(overall, currSum)
        return overall