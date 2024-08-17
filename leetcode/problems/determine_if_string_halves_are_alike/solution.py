class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        str1 = s[:n]
        str2 = s[n:]
        vowel1 = 0
        vowel2 = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(0, n):
            if str1[i] in vowels:
                vowel1 += 1
            if str2[i] in vowels:
                vowel2 += 1
        return vowel1 == vowel2