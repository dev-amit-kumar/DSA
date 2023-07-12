# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Comp : O(2n)
# def lengthOfLongestSubstring(str):
#     if(len(str) == 1):
#         return 1
#     res = 0
#     left = 0
#     right = 0
#     seen = set()
#     count = 0
#     while(left < len(str) and right < len(str)):
#         if(str[right] in seen):
#             seen = set()
#             right = left = left+1
#             count = 0
#         else:
#             seen.add(str[right])
#             count += 1
#             right += 1
#         res = max(res, count)
#     return res


def lengthOfLongestSubstring(str):
    if(len(str) == 1):
        return 1
    res = left = right = 0
    seen = {}
    while(right < len(str)):
        val = str[right]
        if(val in seen):
            left = max(seen[val] + 1, left)
        seen[val] = right
        res = max(res, right - left + 1)
        right += 1
    return res


str = ["bbbbb", "abcabcbb", "aufffgiha", "pwwkew", " ", "au", "dvdf"]
res = [1, 3, 5, 3, 1, 2, 3]
for i in range(0, len(str)):
    out = lengthOfLongestSubstring(str[i])
    if(out != res[i]):
        print(False)
    else:
        print(True)
