// https://leetcode.com/problems/merge-sorted-array/description/

#include<iostream>
#include<vector>

using namespace std;

void bruteForce(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    int i = 0;
    int j = 0;
    int len = nums1.size();
    vector<int> nums3;

    while (i < m && j < n)
    {
        if(nums1[i] <= nums2[j]){
            nums3.push_back(nums1[i]);
            i++;
        }
        else
        {
            nums3.push_back(nums2[j]);
            j++;
        }
    }
    // If right pointer reaches the end:
    while (i < m)
    {
        nums3.push_back(nums1[i]);
        i++;
    }

    // If left pointer reaches the end:
    while (j < n)
    {
        nums3.push_back(nums2[j]);
        j++;
    }

    cout << "Brute force : ";
    for (int i = 0; i < len; i++)
    {
        cout << nums3[i] << " ";
    }
    cout << endl;
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