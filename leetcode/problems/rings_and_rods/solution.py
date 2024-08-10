class Solution:
    def countPoints(self, rings: str) -> int:
        hash_map = {}
        count = 0
        for i in range(0, len(rings), 2):
            color = rings[i]
            index = rings[i+1]
            if index in hash_map:
                hash_map[index] += color
            else:
                hash_map[index] = color
        print(hash_map)
        for i in hash_map:
            make_set = set(hash_map[i])
            if len(make_set) == 3:
                count += 1
        return count
