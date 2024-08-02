class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence_set = set()
        for i in sentence:
            sentence_set.add(i)
        return True if len(sentence_set) == 26 else False