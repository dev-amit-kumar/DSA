class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_no = float('-inf')
        for sentence in sentences:
            wordsList = sentence.split(" ")
            max_no = max(max_no, len(wordsList))
        return max_no