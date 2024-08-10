class Solution {
public:
    int findContentChildren(vector<int>& greed, vector<int>& cookie) {
        sort(greed.begin(), greed.end());
        sort(cookie.begin(), cookie.end());
        int N = greed.size();
        int M = cookie.size();
        int i = N - 1;
        int j = M - 1;
        int count = 0;
        while (i >= 0 && j >= 0)
        {
            if (greed[i] <= cookie[j])
            {
                j--;
                count++;
            }
            i--;
        }
        return count;
    }
};