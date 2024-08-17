class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for w in words:
            for n in words:
                if w != n and w in n:
                    res.add(w)
        return list(res)