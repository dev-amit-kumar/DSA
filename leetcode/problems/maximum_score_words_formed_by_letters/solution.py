class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = Counter(letters)

        def canFormWord(word):
            countW = Counter(word)
            for c in word:
                if countW[c]>count[c]:
                    return False
            return True

        def backtrack(i):
            if i==len(words):
                return 0

            res = backtrack(i+1) #skip
            if canFormWord(words[i]):
                points = 0
                for c in words[i]:
                    count[c]-=1
                    points+=score[ord(c)-ord('a')]
                res=max(res,points+backtrack(i+1))
                for c in words[i]:
                    count[c]+=1
            return res

        return backtrack(0)