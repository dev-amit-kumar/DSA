class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (len(nums1) > len(nums2)):
            return self.intersect(nums2, nums1)
        freq1 = {}
        freq2 = {}
        for i in nums1:
            if i in freq1:
                freq1[i] += 1
            else:
                freq1[i] = 1
        for i in nums2:
            if i in freq2:
                freq2[i] += 1
            else:
                freq2[i] = 1
        result = []
        for key, val1 in freq1.items():
            if key not in freq2:
                continue
            val2 = freq2[key]
            occ = min(val1, val2)
            result += [key] * occ
        return result