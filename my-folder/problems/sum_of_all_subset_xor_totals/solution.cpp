class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int n=nums.size();
        int ans=0;
        for(int i=0;i<n;i++){
            ans|=nums[i];
        }
        return ans*pow(2,n-1);
    }
};