class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hash_map = {}
        for i in range(0, n):
            if nums[i] in hash_map:
                j = hash_map[nums[i]]
                if abs(i-j) <= k:
                    return True
                else:
                    hash_map[nums[i]] = i
            else:
                hash_map[nums[i]] = i
        return False