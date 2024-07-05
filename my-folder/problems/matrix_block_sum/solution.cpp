class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int k) {
        int n=mat.size(),m=mat[0].size();
        vector<vector<int>> temp(n,vector<int>(m));

        for(int i=0;i<n;i++){
            int sum=0;
            for(int j=0;j<m;j++){
                sum+=mat[i][j];
                temp[i][j]=sum;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                int sum=0;
                int ur=max(0,i-k);
                int lr=min(n-1,i+k);
                int lc=max(0,j-k);
                int rc=min(m-1,j+k);
                for(int x=ur;x<=lr;x++){
                    sum+=temp[x][rc];
                    if(lc!=0) sum-=temp[x][lc-1];
                }
                mat[i][j]=sum;
            }
        }
        return mat;
        
    }
};