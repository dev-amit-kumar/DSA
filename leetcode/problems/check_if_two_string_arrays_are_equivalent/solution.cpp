class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string string1 = "";
        string string2 = "";
        int m = word1.size();
        int n = word2.size();
        for (int i = 0; i < m; i++)
            string1 += word1[i];
        for (int j = 0; j < n; j++)
            string2 += word2[j];
        return string1 == string2;
    }
};