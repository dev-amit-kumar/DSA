class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        print(hash)
        total = 0
        for i in nums:
            if hash[i] > 1:
                a = hash[i]
                val = ((a)*(a-1))/2
                total += val
                hash[i] = 0
        return int(total)