class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        result = original
        for i in nums:
            if result in nums:
                result *= 2
            else:
                break
        return result