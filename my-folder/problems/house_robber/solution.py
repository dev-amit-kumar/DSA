class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)        
        a = b = c = 0
        for i in range(n):            
            c = max(a + nums[i], b)                        
            a, b = b, c
        return c