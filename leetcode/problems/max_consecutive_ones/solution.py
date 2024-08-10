class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_no = 0
        for i in nums:
            if i == 1:
                count += 1
                if count >= max_no:
                    max_no = count
            else:
                count = 0
        return max_no
         