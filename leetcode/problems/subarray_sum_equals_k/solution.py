class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0: 1}
        count = 0
        sum_ = 0

        for num in nums:
            sum_ += num
            diff = sum_ - k
            if diff in cache:
                count += cache[diff]
            cache[sum_] = cache.get(sum_, 0) + 1

        return count