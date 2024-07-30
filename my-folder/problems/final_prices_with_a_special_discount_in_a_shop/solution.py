class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = []
        n = len(prices)
        for i in range(n-1, -1, -1):
            while(stack and prices[i] < stack[-1]):
                stack.pop()
            if(not stack):
                ans.append(prices[i])
            else:
                ans.append(prices[i] - stack[-1])
            stack.append(prices[i])
        ans.reverse()
        return ans