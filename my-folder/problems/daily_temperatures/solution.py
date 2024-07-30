class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n
        stack = []
        for i in range(len(temp)-1, -1, -1):
            while(stack and temp[i] >= temp[stack[-1]]):
                stack.pop()
            if (not stack):
                ans[i] = 0
            else:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans