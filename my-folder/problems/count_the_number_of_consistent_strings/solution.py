class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = []
        for word in words:
            currResult = True
            for char in word:
                if char not in allowed:
                    currResult = False
                    break
            if currResult:
                result.append(word)
        # print(result)
        return len(result)