class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        repeat = word
        while(repeat in sequence):
            repeat += word
            count += 1
        return count