class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size();
        int m = needle.size();
        int i = 0;
        while (i < n)
        {
            int j = 0;
            int temp = i;
            if (haystack[i] == needle[j])
            {
                i++;
                j++;
                while (j < m && haystack[i] == needle[j])
                {
                    i++;
                    j++;
                }
                if (j == m)
                    return i - j;
            }
            i = ++temp;
        }
        return -1;
    }
};