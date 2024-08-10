class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        result = ''
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freqArray = []
        charArray = set()
        for key, values in freq.items():
            freqArray.append(values)
            charArray.add(key)
        charArray = sorted(charArray)
        freqArray.sort(reverse=True)
        for i in freqArray:
            for j in charArray:
                if freq[j]==i and j not in result:
                    result+=j*i
                    break
        return result