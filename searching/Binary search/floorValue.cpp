// Link:  https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

#include <iostream>
using namespace std;
int findFloor(int arr[], long long len, long long num)
{
    int start = 0;
    int end = len - 1;
    int mid = (start + end) / 2;
    while (start <= end)
    {
        if (arr[mid] == num)
        {
            return mid;
        }
        else if (arr[mid] < num)
        {
            start = mid + 1;
        }
        else if (arr[mid] > num)
        {
            end = mid - 1;
        }
        mid = (start + end) / 2;
    }
    if (arr[mid] < num)
    {
        return mid;
    }
    return -1;
}

int main()
{
    int arr[7] = {1, 2, 8, 10, 11, 12, 19};
    int val = 13;
    int n = sizeof(arr) / sizeof(arr[0]);
    int response = findFloor(arr, n, val);
    cout << response << endl;
}