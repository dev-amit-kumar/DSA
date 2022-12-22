class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& arr) {
        int n = arr.size();
        int curr_max = 0;
        int total = 0;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == 0)
            {
                total = max(total, curr_max);
                curr_max = 0;
            }
            else
            {
                curr_max++;
            }
        }
        return max(total, curr_max);
    }
};