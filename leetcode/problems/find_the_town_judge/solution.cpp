class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        if (trust.size() == 0 && n == 1) 
            return 1;
        vector<int> trustArray(n+1, 0);
        int len = trust.size();
        for (auto person : trust) {
            trustArray[person[0]]--;
            trustArray[person[1]]++;
        }

        for(int i = 0; i < trustArray.size(); i++){
            if(trustArray[i] == n-1) return i;
        }
        return -1;
    }
};