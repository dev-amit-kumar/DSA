class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map[i] + 1 if i in hash_map else 1
        for i in hash_map:
            if hash_map[i] == 1:
                return s.index(i)
        return -1