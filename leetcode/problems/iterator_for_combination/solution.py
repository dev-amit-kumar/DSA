class CombinationIterator:
    from itertools import combinations

    def __init__(self, characters: str, combinationLength: int):
        self.comb = list(combinations(characters, combinationLength))
        

    def next(self) -> str:
        return ''.join(self.comb.pop(0))

    def hasNext(self) -> bool:
        return len(self.comb)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()