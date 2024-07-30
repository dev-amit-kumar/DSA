class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = {}
        for i in range(len(nums2) - 1, -1, -1):
            while(stack and stack[-1] <= nums2[i]):
                stack.pop()
            if not stack:
                hash_map[nums2[i]] = -1
            else:
                hash_map[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = hash_map[nums1[i]]
        return nums1