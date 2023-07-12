# Link: https://leetcode.com/problems/next-greater-element-i/
def nextGreaterElement(nums):
    dic = {}
    out = []
    for i in range(len(nums)):
        dic[nums[i]] = -1
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                dic[nums[i]] = nums[j]
                break
    print(dic)
    return out

    # size = len(nums)
    # nums += nums
    # res = [-1] * size
    # stack = []
    # for i in list(range(size))*2:
    #     while stack and (nums[stack[-1]] < nums[i]):
    #         res[stack.pop()] = nums[i]
    #     stack.append(i)
    # return res


nums = [1, 2, 3, 4, 3]
output = nextGreaterElement(nums)
print(output)
