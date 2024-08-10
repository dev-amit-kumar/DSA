class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set()
        longest_series = 0
        for i in nums:
            arr.add(i)
        for i in nums:
            if (i - 1) not in arr:
                current_number = i
                current_series = 0
                while(current_number in arr):
                    current_number += 1
                    current_series += 1
                longest_series = max(longest_series, current_series)
        return longest_series
        