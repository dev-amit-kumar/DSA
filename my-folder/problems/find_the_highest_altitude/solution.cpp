class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int n = gain.size();
        int max_alt = 0;
        int last_alt = 0;
        for (int i = 0; i < n; i++){
            last_alt += gain[i];
            max_alt = max(max_alt, last_alt);
        }
        return max_alt;
    }
};