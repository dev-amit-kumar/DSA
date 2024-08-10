class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash_set = set()
        for i in range(len(paths)):
            hash_set.add(paths[i][0])
        for i in range(len(paths)):
            end = paths[i][1]
            if end not in hash_set:
                return end
        return ""