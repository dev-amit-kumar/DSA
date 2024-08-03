class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        doubleSum = 0
        singleSum = 0
        for i in nums:
            if i > 9:
                doubleSum += i
            else:
                singleSum += i
        return True if doubleSum != singleSum else False
        