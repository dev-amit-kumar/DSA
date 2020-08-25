class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        out=[]
        for i in range(len(nums2)):
            dic[nums2[i]]=-1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    dic[nums2[i]]=nums2[j]
                    break
        for k in range(len(nums1)):
            out.append(dic[nums1[k]])
        return out