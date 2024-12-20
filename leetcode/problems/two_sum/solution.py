class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}

        for i in range(n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [i, hash_map[remaining]]
            hash_map[nums[i]] = i

        return []