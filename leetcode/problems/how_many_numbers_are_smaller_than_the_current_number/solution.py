class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNum = sorted(nums)
        freq = {}
        result = []
        for i in range(0, len(sortedNum)):
            val = sortedNum[i]
            if val not in freq:
                freq[val] = i
        for i in nums:
            result.append(freq[i])
        return result