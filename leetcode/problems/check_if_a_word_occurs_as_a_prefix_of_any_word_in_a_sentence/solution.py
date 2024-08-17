class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        n = len(searchWord)
        for i in range(0, len(words)):
            
            if searchWord == words[i][:n]:
                return i+1
        return -1