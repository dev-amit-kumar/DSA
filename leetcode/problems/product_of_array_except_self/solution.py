class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # total = []
        # for i in range(len(nums)):
        #     count = 1
        #     for j in range(len(nums)):
        #         if(i != j):
        #             count *= nums[j]
        #     total.append(count)
        # return total    
        n = len(nums)
        left = [1] * n
        # right = [1] * n
        # ans = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        # for i in range(n-2, -1, -1):
        #     right[i] = right[i+1] * nums[i+1]
        # for i in range(0, n):
        #     ans[i] = left[i] * right[i]
        # return ans
        right = 1
        for i in range(n-1, -1, -1):
            left[i] = left[i] * right
            right = right * nums[i]
        return left
