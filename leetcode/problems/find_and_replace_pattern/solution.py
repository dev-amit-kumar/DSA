class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matching_words = []
        for word in words:
            forward_map = {}
            reverse_map = {}
            is_match = True
            for word_char, pattern_char in zip(word, pattern):
                if pattern_char in forward_map and forward_map[pattern_char] != word_char:
                    is_match = False
                    break
                elif word_char in reverse_map and reverse_map[word_char] != pattern_char:
                    is_match = False
                    break
                else:
                    forward_map[pattern_char] = word_char
                    reverse_map[word_char] = pattern_char
            if is_match:
                matching_words.append(word)
        return matching_words