class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<pair<int,int>> arr;
        for(int i=0; i<mat.size(); i++)
        {
            int c=0;
            for(int j=0; j<mat[i].size(); j++)
            {
                if(mat[i][j] == 1)
                {
                    c++;
                }
            }
            arr.push_back({c, i});
        }

        sort(arr.begin(), arr.end());
        vector<int> res(k, 0);
        for(int i = 0; i < k; i++) 
        {
            res[i] = arr[i].second;
        }
        return res;
    }
};