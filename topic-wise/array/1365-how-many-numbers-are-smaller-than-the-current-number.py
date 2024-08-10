# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

nums = [8,1,2,2,3]
result = []
for i in range(len(nums)):
    curr = 0
    for j in range(0, len(nums)):
        if (nums[i] > nums[j] and i != j):
            curr += 1
    result.append(curr)
print(result)