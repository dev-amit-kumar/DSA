class Solution:
    def isValid(self, num, price):
        count = 1
        diff = price[0] + num
        for i in price:
            if i >= diff:
                count += 1
                diff = num + i
        return count

    def maximumTastiness(self, price: List[int], k: int) -> int:
        if k == 0:
            return 0
        price.sort()
        low = 0
        high = price[-1] - price[0]
        ans = -1
        while(low <= high):
            mid = (low + high) // 2
            if(self.isValid(mid, price) >= k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans