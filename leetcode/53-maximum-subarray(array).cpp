// https://leetcode.com/problems/maximum-subarray/

// Kadane’s Algorithm
// Step 1: Initialize the variables overallMax = INT_MIN and currSum = 0
// Step 2: Run a for loop from 0 to N-1 and for each index i:
//     Step a: Add the arr[i] to currSum.
//     Step b: If  overallMax is less than currSum then update overallMax  to currSum.
//     Step c: If currSum < 0 then update currSum = 0
// Step 4: Return overallMax

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int currSum = 0;
        int overallMax = INT_MIN;
        int len = nums.size();
        for (int i = 0; i < len; i++)
        {
            if (nums[i] + currSum > nums[i])
                currSum += nums[i];
            else
                currSum = nums[i];
            if (currSum > overallMax)
                overallMax = currSum;
        }
        return overallMax;
    }
};