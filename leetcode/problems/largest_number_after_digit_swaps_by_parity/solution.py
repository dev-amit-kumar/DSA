class Solution:
    def largestInteger(self, num: int) -> int:
        even, odd = [], []
        nums = [-int(n) for n in str(num)]
        for n in nums:
            heapq.heappush(even if n % 2 else odd, n)
        result = 0
        for n in nums:
            x = heapq.heappop(even if n % 2 else odd)
            print(x)
            result = result * 10 + (-x)
        return result