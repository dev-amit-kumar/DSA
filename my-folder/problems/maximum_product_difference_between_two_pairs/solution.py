class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:
        smallest, second_smallest = float('inf'), float('inf')
        highest, second_highest = float('-inf'), float('-inf')
        for i in nums:
            if i > highest:
                second_highest = highest
                highest = i
            elif i > second_highest:
                second_highest = i
            if i < smallest:
                second_smallest = smallest
                smallest = i
            elif i < second_smallest:
                second_smallest = i
        return (highest * second_highest) - (smallest * second_smallest)