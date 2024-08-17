class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        newList = []
        for word in words:
            newList.append(word[::-1])
        return ' '.join(newList)