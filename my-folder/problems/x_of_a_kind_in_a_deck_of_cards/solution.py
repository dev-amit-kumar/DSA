class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cache = Counter(deck)

        if len(cache) == 1:
            return cache[deck[0]] > 1

        x = cache[deck[0]]

        for num in cache.values():
            x = gcd(x, num)

        return x > 1