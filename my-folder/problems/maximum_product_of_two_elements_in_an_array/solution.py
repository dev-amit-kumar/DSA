class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest, second_highest = float('-inf'), float('-inf')
        for i in nums:
            if i > highest:
                second_highest = highest
                highest = i
            elif i > second_highest:
                second_highest = i
        return (highest - 1) * (second_highest - 1)