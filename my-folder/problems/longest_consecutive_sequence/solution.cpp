class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        unordered_set<int> s;
        int currCount = 1;
        int lngCount = 1;
        for(int i = 0; i < n; i++)
            s.insert(nums[i]);
        int x = 0;
        for(auto a : s ){
            if(s.find(a-1) == s.end()){
                currCount = 1;
                x = a;
                while(s.find(x+1) != s.end()){
                    currCount+=1;
                    x+=1;
                }
            }
            lngCount = max(lngCount, currCount);
        }
        return lngCount;
    }
};