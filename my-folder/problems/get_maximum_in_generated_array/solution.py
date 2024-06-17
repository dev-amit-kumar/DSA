class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        nums = [0, 1]
        result = 1
        for i in range(2, n+1):
            j = i // 2
            element = nums[j]
            if (i % 2):
                element += nums[j+1]
            result = max(result, element)
            nums.append(element)
        return result