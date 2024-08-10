class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        if(len(nums1) < len(nums2)):
            return self.intersection(nums2, nums1)
        for i in nums2:
            if(i in nums1 and i not in arr):
                arr.append(i)
        return arr