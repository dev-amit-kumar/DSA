// https://leetcode.com/problems/next-permutation/

// Eg
// 2 1 5 4 3 0 0
// 2 3 1 0 0 4 5
// 2 3 1 0 0 5 4

// To find the next permutation we need 4 steps
// Step 1: Find the breakPoint where the series can be split in two piece such that the value of index i is smaller than value at index+1. Find this breakPoint from the end of the list.
// Step 2: If no breakPoint is there, return the reverse of the array
// Step 3: If breakPoint is there, then swap the value which is just bigger than the value at breakPoint. Run the loop from end of the list.
// Step 4: Reverse the array starting from breakPoint to end of the list

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int len = nums.size();
        int breakPoint = -1;
        for (int i = len - 2; i >= 0 ; i--){
            if(nums[i] < nums[i+1]){
                breakPoint = i;
                break;
            }
        }
        if(breakPoint == -1){
            reverse(nums.begin(), nums.end());
            return;
        }
        for(int i = len - 1; i >= breakPoint; i--){
            if (nums[i] > nums[breakPoint])
            {
                swap(nums[i], nums[breakPoint]);
                break;
            }
        }
        reverse(nums.begin() + breakPoint + 1, nums.end());
        return;
    }
};