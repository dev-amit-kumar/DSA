// Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool arrayStringsAreEqual(vector<string> &word1, vector<string> &word2)
{
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

int main()
{
    vector<string> word1;
    word1.push_back("ab");
    word1.push_back("c");

    vector<string> word2;
    word2.push_back("a");
    word2.push_back("bc");

    bool ans = arrayStringsAreEqual(word1, word2);
    cout << "ans " << ans << endl;
}