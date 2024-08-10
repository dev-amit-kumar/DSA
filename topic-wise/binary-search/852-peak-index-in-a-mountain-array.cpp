// https://leetcode.com/problems/peak-index-in-a-mountain-array/

#include <iostream>
#include <vector>
using namespace std;

int linearSearch(vector<int> &arr)
{
    int len = arr.size();
    int i;
    for (i = 1; i < len - 1; i++)
        if (arr[i + 1] < arr[i] and arr[i] > arr[i - 1])
            break;
    return i;
}

int binarySearch(vector<int> &arr)
{
    int n = arr.size();
    int start = 0;
    int end = n - 1;
    int mid = (start + end) / 2;
    while (start < end)
    {
        mid = (start + end) / 2;
        if (arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1])
            return mid;
        if (arr[mid - 1] < arr[mid])
            start = mid;
        else if (arr[mid] > arr[mid + 1])
            end = mid;
    }
    return mid;
}

void peakIndexInMountainArray(vector<int> &arr)
{
    int linearSearchResult = linearSearch(arr);
    cout << "linearSearchResult: " << linearSearchResult << endl;

    int binarySearchResult = binarySearch(arr);
    cout << "binarySearchResult: " << binarySearchResult << endl;
}

int main()
{
    vector<int> arr = {10, 8, 6, 5, 3, 2};
    peakIndexInMountainArray(arr);
}