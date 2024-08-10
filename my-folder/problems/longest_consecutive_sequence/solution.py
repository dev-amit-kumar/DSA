class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        st = set(nums)
        lng = 1
        for i in st:
            if i-1 in st:
                continue
            x = i
            cnt = 1
            while x+1 in st:
                cnt += 1
                x += 1
            lng = max(lng, cnt)
        return lng
            