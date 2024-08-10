class Solution:
    def sortSentence(self, string: str) -> str:
        newString = [0] * len(string.split())

        for chars in string.split():
            newString[int(chars[-1])-1] = chars[:-1]

        return ' '.join(newString)