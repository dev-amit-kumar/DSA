class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        for i in range(0, len(word)):
            if word[i] == ch:
                prefix = word[:i+1]
                prefix = prefix[::-1]
                return prefix + word[i+1:]