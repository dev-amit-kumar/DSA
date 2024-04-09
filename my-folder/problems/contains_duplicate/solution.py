class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for i in nums:
            if i in found:
                return True
            found.add(i)
        return False