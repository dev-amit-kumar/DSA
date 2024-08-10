// https://leetcode.com/problems/merge-sorted-array/description/

#include<iostream>
#include<vector>

using namespace std;

void bruteForce(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    int i = 0, j = 0;
    
}

void optimal(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    
}

int main()
{
    vector<int> nums1 = { 1, 2, 3, 0, 0, 0 };
    vector<int> nums2 = { 2, 5, 6 };
    int m = 3, n = 3;
    bruteForce(nums1, m, nums2, n);
    optimal(nums1, m, nums2, n);
    int fullLength = nums1.size();
    cout << "Optimal : ";
    for(int i = 0; i < fullLength; i++){
        cout << nums1[i] << " ";
    }
    cout << endl;
}