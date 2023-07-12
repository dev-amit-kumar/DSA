// https://leetcode.com/problems/trapping-rain-water/

#include <iostream>
using namespace std;

void bruteForce(int arr[], int n)
{
    int total = 0;
    for (int i = 0; i < n; i++)
    {
        int left = arr[i];
        int right = arr[i];

        for (int j = 0; j < i + 1; j++)
            left = max(left, arr[j]);

        for (int j = i + 1; j < n; j++)
            right = max(right, arr[j]);

        total += min(left, right) - arr[i];
    }
    cout << total << endl;
    // Time Complexity - O(n*n)
    // Space Complexity - O(1)
}

void Precalculation(int arr[], int n)
{
    int leftArray[n];
    int rightArray[n];
    int total = 0;
    leftArray[0] = arr[0];
    for (int i = 0; i < n; i++)
        leftArray[i] = max(leftArray[i - 1], arr[i]);
    rightArray[n - 1] = arr[n - 1];
    for (int i = n - 2; i >= 0; i--)
        rightArray[i] = max(rightArray[i + 1], arr[i]);
    for (int i = 0; i < n; i++)
        total += min(leftArray[i], rightArray[i]) - arr[i];
    cout << total << endl;
    // Time Complexity - O(n)
    // Space Complexity - O(n)
}

int main()
{
    // int arr[] = {3, 0, 2, 0, 4};
    int arr[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    bruteForce(arr, n);
    Precalculation(arr, n);
}
