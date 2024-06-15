class Solution:
    def checkPalindrome(self, word: str) -> bool:
        first = 0
        last = len(word)-1
        while(first < last):
            if(word[first] != word[last]):
                return False
                break
            first += 1
            last -= 1
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            isValid = self.checkPalindrome(word)
            if (isValid):
                return word
        return ""