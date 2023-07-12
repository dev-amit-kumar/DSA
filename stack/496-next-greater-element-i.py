# Link: https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(nums1, nums2):
    dic = {}
    out = []
    for i in range(len(nums2)):
        dic[nums2[i]] = -1
        for j in range(i+1, len(nums2)):
            if nums2[j] > nums2[i]:
                dic[nums2[i]] = nums2[j]
                break
    for k in range(len(nums1)):
        out.append(dic[nums1[k]])
    return out


# def nextGreaterElement(nums1, nums2):
#     stack = list()
#     vector = list()
#     answer = []
#     for i in range(len(nums2)-1, -1, -1):
#         while len(stack) > 0 and stack[-1] <= nums2[i]:
#             stack.pop()
#         if len(stack) == 0:
#             vector.append(-1)
#         else:
#             vector.append(stack[-1])
#         stack.append(nums2[i])
#     vector2 = vector[::-1]
#     for i in nums1:
#         answer.append(vector2[nums2.index(i)])
#     return answer


nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]
output = nextGreaterElement(nums1, nums2)
print(output)
