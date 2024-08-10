class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_arr = [0] * n 
        sufix_arr = [0] * n
        prefix_arr[0] = height[0]
        sufix_arr[n-1] = height[n-1]
        for i in range(1, n):
            prefix_arr[i] = max(prefix_arr[i-1], height[i])
        for i in range(n-2, -1, -1):
            sufix_arr[i] = max(sufix_arr[i+1], height[i])
        result = 0
        for i in range(0, n):
            result += min(prefix_arr[i], sufix_arr[i]) - height[i]
        return result