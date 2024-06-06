class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for i in nums: 
            if i-k in hash_map:
                count+=hash_map[i-k]
        return count