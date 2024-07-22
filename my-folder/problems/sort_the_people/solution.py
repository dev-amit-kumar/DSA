class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        hash_map = {}
        for i in range(0, n):
            hash_map[heights[i]] = names[i]

        heights.sort(reverse=True)
        for i in range(0, n):
            names[i] = hash_map[heights[i]]
        return names