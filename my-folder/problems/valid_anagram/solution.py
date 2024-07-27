class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        for i in s:
            if i in hash_map_s:
                hash_map_s[i] += 1
            else:
                hash_map_s[i] = 1
        hash_map_t = {}
        for i in t:
            if i in hash_map_t:
                hash_map_t[i] += 1
            else:
                hash_map_t[i] = 1
        return hash_map_s == hash_map_t
